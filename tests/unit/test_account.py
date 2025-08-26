"""
Unit tests for the Account class.
"""

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

from ai_stock_trader.accounts.account import Account, Transaction


class TestTransaction:
    """Test the Transaction model."""
    
    def test_transaction_creation(self):
        """Test creating a transaction."""
        transaction = Transaction(
            symbol="AAPL",
            quantity=10,
            price=150.0,
            timestamp="2024-01-01 10:00:00",
            rationale="Test purchase"
        )
        
        assert transaction.symbol == "AAPL"
        assert transaction.quantity == 10
        assert transaction.price == 150.0
        assert transaction.total() == 1500.0
    
    def test_transaction_total_calculation(self):
        """Test transaction total calculation."""
        transaction = Transaction(
            symbol="GOOGL",
            quantity=5,
            price=200.0,
            timestamp="2024-01-01 10:00:00",
            rationale="Test purchase"
        )
        
        assert transaction.total() == 1000.0
    
    def test_transaction_repr(self):
        """Test transaction string representation."""
        transaction = Transaction(
            symbol="MSFT",
            quantity=20,
            price=300.0,
            timestamp="2024-01-01 10:00:00",
            rationale="Test purchase"
        )
        
        expected = "20 shares of MSFT at 300.0 each."
        assert str(transaction) == expected


class TestAccount:
    """Test the Account model."""
    
    @patch('ai_stock_trader.accounts.account.read_account')
    @patch('ai_stock_trader.accounts.account.write_account')
    def test_account_creation_new(self, mock_write, mock_read):
        """Test creating a new account."""
        mock_read.return_value = None
        
        account = Account.get("test_user")
        
        assert account.name == "test_user"
        assert account.balance == 10000.0
        assert account.holdings == {}
        assert account.transactions == []
        assert account.portfolio_value_time_series == []
        mock_write.assert_called_once()
    
    @patch('ai_stock_trader.accounts.account.read_account')
    @patch('ai_stock_trader.accounts.account.write_account')
    def test_account_creation_existing(self, mock_write, mock_read):
        """Test loading an existing account."""
        existing_data = {
            "name": "existing_user",
            "balance": 5000.0,
            "strategy": "conservative",
            "holdings": {"AAPL": 10},
            "transactions": [],
            "portfolio_value_time_series": []
        }
        mock_read.return_value = existing_data
        
        account = Account.get("existing_user")
        
        assert account.name == "existing_user"
        assert account.balance == 5000.0
        assert account.strategy == "conservative"
        assert account.holdings == {"AAPL": 10}
        mock_write.assert_not_called()
    
    @patch('ai_stock_trader.accounts.account.write_account')
    def test_account_save(self, mock_write):
        """Test saving an account."""
        account = Account(
            name="test_user",
            balance=10000.0,
            strategy="aggressive",
            holdings={},
            transactions=[],
            portfolio_value_time_series=[]
        )
        
        account.save()
        mock_write.assert_called_once_with("test_user", account.model_dump())
    
    def test_account_reset(self):
        """Test resetting an account."""
        account = Account(
            name="test_user",
            balance=5000.0,
            strategy="old_strategy",
            holdings={"AAPL": 10},
            transactions=[Transaction(
                symbol="AAPL",
                quantity=10,
                price=150.0,
                timestamp="2024-01-01 10:00:00",
                rationale="Old purchase"
            )],
            portfolio_value_time_series=[("2024-01-01", 5000.0)]
        )
        
        with patch.object(account, 'save') as mock_save:
            account.reset("new_strategy")
            
            assert account.balance == 10000.0
            assert account.strategy == "new_strategy"
            assert account.holdings == {}
            assert account.transactions == []
            assert account.portfolio_value_time_series == []
            mock_save.assert_called_once()
    
    def test_account_deposit(self):
        """Test depositing funds."""
        account = Account(
            name="test_user",
            balance=1000.0,
            strategy="conservative",
            holdings={},
            transactions=[],
            portfolio_value_time_series=[]
        )
        
        with patch.object(account, 'save') as mock_save:
            account.deposit(500.0)
            
            assert account.balance == 1500.0
            mock_save.assert_called_once()
    
    def test_account_deposit_invalid_amount(self):
        """Test depositing invalid amount."""
        account = Account(
            name="test_user",
            balance=1000.0,
            strategy="conservative",
            holdings={},
            transactions=[],
            portfolio_value_time_series=[]
        )
        
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            account.deposit(-100.0)
        
        assert account.balance == 1000.0  # Balance unchanged
    
    def test_account_withdraw(self):
        """Test withdrawing funds."""
        account = Account(
            name="test_user",
            balance=1000.0,
            strategy="conservative",
            holdings={},
            transactions=[],
            portfolio_value_time_series=[]
        )
        
        with patch.object(account, 'save') as mock_save:
            account.withdraw(300.0)
            
            assert account.balance == 700.0
            mock_save.assert_called_once()
    
    def test_account_withdraw_insufficient_funds(self):
        """Test withdrawing more than available balance."""
        account = Account(
            name="test_user",
            balance=1000.0,
            strategy="conservative",
            holdings={},
            transactions=[],
            portfolio_value_time_series=[]
        )
        
        with pytest.raises(ValueError, match="Insufficient funds for withdrawal"):
            account.withdraw(1500.0)
        
        assert account.balance == 1000.0  # Balance unchanged


if __name__ == "__main__":
    pytest.main([__file__])
