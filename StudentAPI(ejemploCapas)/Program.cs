using Microsoft.EntityFrameworkCore;
using StudentAPI.Services;
using StudentAPI.Interfaces;
using StudentAPI.Data;

var builder = WebApplication.CreateBuilder(args);

// Agregar DbContext
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseInMemoryDatabase("StudentDB"));

// Registrar servicios e interfaces
builder.Services.AddScoped<IStudentRepository, StudentRepository>();
builder.Services.AddScoped<IStudentService, StudentService>();

// Agregar controladores
builder.Services.AddControllers();

var app = builder.Build();

app.UseAuthorization();
app.MapControllers();
app.Run();
