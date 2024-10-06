from unittest.mock import patch
from mylib.query import create_record, read_data, update_record, delete_record

def test_create_record():
    with patch('mylib.query.create_record') as mock_create:
        mock_create.return_value = True
        
        result = create_record(1999, 11, 17, 3, 77777)

        mock_create.assert_called_once_with(1999, 11, 17, 3, 77777)
        assert result is True

def test_read_data():
    with patch('mylib.query.read_data') as mock_read:
        mock_read.return_value = [('row1',), ('row2',)]

        data = read_data()

        mock_read.assert_called_once()
        assert data == [('row1',), ('row2',)]

def test_update_record():
    with patch('mylib.query.update_record') as mock_update:
        mock_update.return_value = True
        
        result = update_record(7, 2000, 1, 1, 6, 9100)

        mock_update.assert_called_once_with(7, 2000, 1, 1, 6, 9100)
        assert result is True

def test_delete_record():
    with patch('mylib.query.delete_record') as mock_delete:
        mock_delete.return_value = True

        result = delete_record(8)

        mock_delete.assert_called_once_with(8)
        assert result is True

if __name__ == "__main__":
    test_create_record()
    test_read_data()
    test_update_record()
    test_delete_record()