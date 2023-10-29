using Dapper;
using TestWebAPI.Endpoints;
using TestWebAPI.Models;
using TestWebAPI.Services;

//development variables

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddSingleton(serviceProvider =>
{
    var configuration = serviceProvider.GetRequiredService<IConfiguration>();

    /*gets the connection config string from the JSON file.
    In this case, this file is the appsettings.Development.json */
    var connectionString = configuration.GetConnectionString("DefaultConnection") ??
                           throw new ApplicationException("The connection string is null");

    //returns the connection
    return new SqlConnectionFactory(connectionString);
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapCustomerEndpoints();
// runs the API program
app.Run();