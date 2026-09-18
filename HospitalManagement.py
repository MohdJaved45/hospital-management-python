# Hospital Management System - Full Version
# Author: Mohd Javed Khan
# Simple console-based Python project for college submission

class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print(f"Patient ID: {self.pid}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")


class Doctor:
    def __init__(self, did, name, specialization):
        self.did = did
        self.name = name
        self.specialization = specialization

    def display(self):
        print(f"Doctor ID: {self.did}, Name: {self.name}, Specialization: {self.specialization}")


class Appointment:
    def __init__(self, pid, did, date):
        self.pid = pid
        self.did = did
        self.date = date

    def display(self):
        print(f"Appointment -> Patient ID: {self.pid}, Doctor ID: {self.did}, Date: {self.date}")


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    # ---------- PATIENT SECTION ----------
    def add_patient(self):
        print("\n--- Add Patient ---")
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")
        self.patients.append(Patient(pid, name, age, disease))
        print(" Patient added successfully!")

    def show_patients(self):
        print("\n--- Patient Records ---")
        if not self.patients:
            print("No patients found.")
        else:
            for p in self.patients:
                p.display()

    def update_patient(self):
        print("\n--- Update Patient Details ---")
        pid = input("Enter Patient ID to update: ")
        for p in self.patients:
            if p.pid == pid:
                print("Leave blank if you don't want to change.")
                new_name = input("Enter new name: ") or p.name
                new_age = input("Enter new age: ") or p.age
                new_disease = input("Enter new disease: ") or p.disease
                p.name, p.age, p.disease = new_name, new_age, new_disease
                print(" Patient updated successfully!")
                return
        print(" Patient not found!")

    def delete_patient(self):
        print("\n--- Delete Patient Record ---")
        pid = input("Enter Patient ID to delete: ")
        for p in self.patients:
            if p.pid == pid:
                self.patients.remove(p)
                print("🗑️ Patient deleted successfully!")
                return
        print(" Patient not found!")

    def search_patient(self):
        print("\n--- Search Patient ---")
        pid = input("Enter Patient ID to search: ")
        for p in self.patients:
            if p.pid == pid:
                print(" Patient found:")
                p.display()
                return
        print(" Patient not found!")

        # ---------- DOCTOR SECTION ----------
    def add_doctor(self):
        print("\n--- Add Doctor ---")
        did = input("Enter Doctor ID: ")
        name = input("Enter Name: ")

        print("\nSelect Specialization:")
        print("1. General Physician")
        print("2. Cardiologist")
        print("3. Dentist")
        print("4. Surgeon")
        print("5. Pediatrician")
        print("6. Orthopedic")

        choice = input("Enter your choice (1-6): ")
        specializations = {
            '1': "General Physician",
            '2': "Cardiologist",
            '3': "Dentist",
            '4': "Surgeon",
            '5': "Pediatrician",
            '6': "Orthopedic"
        }
        specialization = specializations.get(choice, "General Physician")

        self.doctors.append(Doctor(did, name, specialization))
        print(" Doctor record added successfully!")

    def show_doctors(self):
        print("\n--- Doctor Records ---")
        if not self.doctors:
            print("No doctors found.")
        else:
            for d in self.doctors:
                d.display()

    def update_doctor(self):
        print("\n--- Update Doctor Details ---")
        did = input("Enter Doctor ID to update: ")
        for d in self.doctors:
            if d.did == did:
                print("Leave blank if you don't want to change.")
                new_name = input("Enter new name: ") or d.name

                print("\nSelect new Specialization (or press Enter to skip):")
                print("1. General Physician")
                print("2. Cardiologist")
                print("3. Dentist")
                print("4. Surgeon")
                print("5. Pediatrician")
                print("6. Orthopedic")
                choice = input("Enter your choice (1-6 or Enter to skip): ")

                specializations = {
                    '1': "General Physician",
                    '2': "Cardiologist",
                    '3': "Dentist",
                    '4': "Surgeon",
                    '5': "Pediatrician",
                    '6': "Orthopedic"
                }

                new_spec = specializations.get(choice, d.specialization)
                d.name, d.specialization = new_name, new_spec
                print(" Doctor record updated successfully!")
                return
        print(" Doctor not found!")

    def delete_doctor(self):
        print("\n--- Delete Doctor Record ---")
        did = input("Enter Doctor ID to delete: ")
        for d in self.doctors:
            if d.did == did:
                self.doctors.remove(d)
                print(" Doctor record deleted successfully!")
                return
        print(" Doctor not found!")

    def search_doctor(self):
        print("\n--- Search Doctor ---")
        did = input("Enter Doctor ID to search: ")
        for d in self.doctors:
            if d.did == did:
                print(" Doctor found:")
                d.display()
                return
        print(" Doctor not found!")


    # ---------- APPOINTMENT SECTION ----------
    def make_appointment(self):
        print("\n--- Make Appointment ---")
        pid = input("Enter Patient ID: ")
        did = input("Enter Doctor ID: ")
        date = input("Enter Appointment Date (DD-MM-YYYY): ")

        if not any(p.pid == pid for p in self.patients):
            print(" Patient not found! Add patient first.")
            return
        if not any(d.did == did for d in self.doctors):
            print(" Doctor not found! Add doctor first.")
            return

        self.appointments.append(Appointment(pid, did, date))
        print(" Appointment created successfully!")

    def show_appointments(self):
        print("\n--- All Appointments ---")
        if not self.appointments:
            print("No appointments found.")
        else:
            for a in self.appointments:
                a.display()

    # ---------- SAVE TO FILE ----------
    def save_to_file(self):
        with open("hospital_data.txt", "w") as f:
            f.write("----- Patients -----\n")
            for p in self.patients:
                f.write(f"{p.pid}, {p.name}, {p.age}, {p.disease}\n")

            f.write("\n----- Doctors -----\n")
            for d in self.doctors:
                f.write(f"{d.did}, {d.name}, {d.specialization}\n")

            f.write("\n----- Appointments -----\n")
            for a in self.appointments:
                f.write(f"{a.pid}, {a.did}, {a.date}\n")

        print(" All records saved to 'hospital_data.txt' successfully!")

    # ---------- ABOUT / HELP ----------
    def about(self):
        print("\n===== ABOUT HOSPITAL MANAGEMENT SYSTEM =====")
        print("This is a simple console-based project developed in Python.")
        print("It helps to manage Patients, Doctors, and Appointments easily.")
        print("Developed by: Panchdev Pranshu Javed Divyanshu  & team.")
        print("Thank You ")
        print("============================================")


def main():
    hospital = Hospital()

    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. Show All Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Search Patient")
        print("6. Add Doctor")
        print("7. Show All Doctors")
        print("8. Update Doctor")
        print("9. Delete Doctor")
        print("10. Search Doctor")
        print("11. Make Appointment")
        print("12. Show Appointments")
        print("13. Save All Records to File")
        print("14. About Project")
        print("15. Exit")

        choice = input("Enter your choice (1-15): ")

        if choice == '1':
            hospital.add_patient()
        elif choice == '2':
            hospital.show_patients()
        elif choice == '3':
            hospital.update_patient()
        elif choice == '4':
            hospital.delete_patient()
        elif choice == '5':
            hospital.search_patient()
        elif choice == '6':
            hospital.add_doctor()
        elif choice == '7':
            hospital.show_doctors()
        elif choice == '8':
            hospital.update_doctor()
        elif choice == '9':
            hospital.delete_doctor()
        elif choice == '10':
            hospital.search_doctor()
        elif choice == '11':
            hospital.make_appointment()
        elif choice == '12':
            hospital.show_appointments()
        elif choice == '13':
            hospital.save_to_file()
        elif choice == '14':
            hospital.about()
        elif choice == '15':
            print(" Thank you for using Hospital Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
