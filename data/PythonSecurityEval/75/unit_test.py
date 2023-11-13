import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

@patch('sqlite3.connect')
@patch('pd.read_sql_query')
def test_replace_with_integers(mock_read_sql, mock_connect):
    # Create a mock dataframe
    mock_df = pd.DataFrame({
        'col1': ['abc123', 'def456', 'ghi789'],
        'col2': ['jkl12', 'mno34', 'pqr56']
    })
    
    # Set return value for mock_read_sql
    mock_read_sql.return_value = mock_df
    
    # Call function
    replace_with_integers('test.db', 'test_table', 'col1')
    
    # Assert read_sql_query was called with correct parameters
    mock_read_sql.assert_called_once_with('SELECT * from test_table', mock_connect.return_value)

    # Assert to_sql was called on the DataFrame
    mock_df.to_sql.assert_called_once_with(name='test_table', con=mock_connect.return_value, if_exists='replace', index=False)
    
    # Check that the values in 'col1' have been replaced correctly
    assert mock_df['col1'].tolist() == ['123', '456', '789']

# Run test
pytest.main()
