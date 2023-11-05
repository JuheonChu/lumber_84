using MySqlConnector;



namespace TestWebAPI.Services
{
    //Helper method to perform the connectiopn to the MySQL database
    public class SqlConnectionFactory
    {
        //the connection string with the connection credentials and information
        private readonly string _connectionString;

        //injection of the connection string
        public SqlConnectionFactory(string connectionString)
        {
            _connectionString = connectionString;
        }

        //creates the connection to the database
        public MySqlConnection Create()
        {
            return new MySqlConnection(_connectionString);
        }
    }
}
