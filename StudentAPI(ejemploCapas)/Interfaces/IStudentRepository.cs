using StudentAPI.Models;

namespace StudentAPI.Interfaces
{
    public interface IStudentRepository
    {
        Student GetById(int id);
        void Add(Student student);
    }
}
