package lumberTry;

public class SchoolClass {
	
	int studentNumber;
	int classRoom;
	String teacherName;
	
	public SchoolClass(int studentNumber, int classRoom, String teacherName) {
		this.classRoom = classRoom;
		this.studentNumber = studentNumber;
		this.teacherName = teacherName;
	}
	
	public void addStudent() {
		studentNumber ++;
	}
	
	public void classRoomNum(int classRoomNumber) {
		classRoom = classRoomNumber;
	}
	
	public static void main(String args[]) {
		SchoolClass CS = new SchoolClass(20,118,"Goble William");
		CS.addStudent();
		
	}

}
