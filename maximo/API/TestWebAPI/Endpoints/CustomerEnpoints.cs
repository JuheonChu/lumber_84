using Dapper;
using Microsoft.Extensions.Configuration;
using TestWebAPI.Models;
using TestWebAPI.Services;

namespace TestWebAPI.Endpoints
{
    //This class will hold all of the customer request methods
    public static class CustomerEnpoints
    {
        public static void MapCustomerEndpoints(this IEndpointRouteBuilder builder)
        {
            //simplifies the initial /users route since it applies to all of the endpoints
            var group = builder.MapGroup("users");

            //this request method retrieves all users from the database
            group.MapGet("", async (SqlConnectionFactory sqlConnectionFactory) =>
            {
                /* Connection variable where we establish our connection with the MySQL
                database */
                using var connection = sqlConnectionFactory.Create();

                //SQL query to request data from database
                const string sql = "SELECT id_users, username, password, email FROM users";

                /* This line will send a connection request to with the SQL
                query we created. Customer is the file where we established
                the variables we want to retrieve from the database*/
                var users = await connection.QueryAsync<Customer>(sql);

                //returns the values from the query request made above
                return Results.Ok(users);
            });

            /*this request method will retrieve the selected user (that will be chose by passing
            its respective id_users)*/
            group.MapGet("{id}", async (int id, SqlConnectionFactory sqlConnectionFactory) =>
            {

                using var connection = sqlConnectionFactory.Create();

                const string sql = """
                    SELECT id_users, username, password, email 
                    FROM users
                    WHERE id_users = @UserId
                    """;

                var user = await connection.QuerySingleOrDefaultAsync<Customer>(
                    sql,
                    new { UserId = id });

                return user is not null ? Results.Ok(user) : Results.NotFound();
            });

            /*this request method will create a new user in the database by passing all
             the desired input values into the body of the request*/
            group.MapPost("", async (Customer user, SqlConnectionFactory sqlConnectionFactory) =>
            {
                using var connection = sqlConnectionFactory.Create();
                
                //This sql query inserts the values shown in the VALUES into the users table
                //notice that the values that we're adding have @ before their names
                const string sql = """
                    INSERT INTO users (username, password, email)
                    VALUES (@username, @password, @email)
                """;

                await connection.ExecuteAsync(sql, user);

                return Results.Ok();
            });

            /*this mehtod will update the selected user (that's selected by passing its id_users
             into the request) by passing all the desired input values into the body of the request*/
            group.MapPut("{id}", async (int id, Customer user, SqlConnectionFactory sqlConnectionFactory) =>
            {
                using var connection = sqlConnectionFactory.Create();

                //assigns the @id_users value the id parameter we pass onto the builder
                user.id_users = id;

                const string sql = """
                    UPDATE users
                    SET username = @username, 
                        password = @password, 
                        email = @email
                    WHERE id_users = @id_users
                """;

                await connection.ExecuteAsync(sql, user);

                return Results.NoContent();
            });

            /*this request will delete the selected user (that's selected by passing the
             id_users into the request)*/
            builder.MapDelete("{id}", async (int id, SqlConnectionFactory sqlConnectionFactory) =>
            {
                using var connection = sqlConnectionFactory.Create();

                const string sql = "DELETE FROM users WHERE id_users = @UserId";

                await connection.ExecuteAsync(sql, new { UserId = id });

                return Results.NoContent();
            });
        }
    }
}
