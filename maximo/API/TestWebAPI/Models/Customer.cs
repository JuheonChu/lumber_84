namespace TestWebAPI.Models
{

    //Class which will store the values (VARIABLES NEED TO HAVE THE SAME NAMES AS THE
    //FIELDS IN THE TABLE) retrieved from the database. In this case we're retrieving
    //the users' data from the users table in the database.
    public class Customer
    {
        public int id_users { get; set; }

        public string username { get; set; }

        public string password { get; set; }
        public string email { get; set; }
    }
}
