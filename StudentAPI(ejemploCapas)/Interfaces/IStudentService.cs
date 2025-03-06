using StudentAPI.Models;

namespace StudentAPI.Interfaces
{
    public interface IStudentService
    {
        Student GetStudentById(int id);
        void AddStudent(Student student);
    }
}
