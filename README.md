## 🏨 HostelSphere
**HostelSphere** is a full-stack **hostel management web application** built using **Python Flask, MySQL, and HTML/CSS**, inspired by real-life hostel challenges people face.
 - #### Problems faced by Hostel:

   - No resident database
    
   - Manual form verification and its storage

   - Unchecked fee status
 
   - No interaction with residents
 
 - #### Problems faced by Residents:
   - Delay in services ( cleaning, repairment, electrical failure, wifi problems)
    
   - No transparency in work, irregular room allotments
 
   - Have to meet personally to raise Complaints


   ## What we offer:
     - From **"Register as a Resident"** section, fill your details only once and generate your **"Unique Resident  ID"**
  
     - Give that **Resident ID** to your **Hostel Incharge** (**HOSTEL MUST BE REGISTERED TO HOSTELSPHERE**)
  
     - **Hostel Incharge** adds you to their hostel. Use **login as Resident**, fill resident username and password, gets you to your dashboard.
  
     - No paper work, no personal meet, fast, efficient and transparent
       
     - ### Want to change your Hostel?
       
        - **Logout --> give the same Resident ID to the new Hostel --> get added.**


---

## 🚀 Features


- Role-based system for **Hostel Incharge and Residents**

- **Auto-generated unique IDs**

    - **Hostel ID:** SPHERE0001, SPHERE0002, …

    - **Resident ID:** RES0001, RES0002, …

- **Secure password authentication**


- Hostel dashboard to:


    - View residents of the hostel


    - Add residents using Resident ID

    - Give updates
 
    - Read resident complaints

- Resident dashboard to:


    - View assigned hostel

    - Get latest updates and notices
      
    - Raise complaints from anywhere. No personal meet required


- Simple and clean user interface

---

## 🛠 Tech Stack



**Frontend**: HTML, CSS


**Backend**: Python (Flask)


**Database**: MySQL

---

## 🗄 Database Structure



**hostels** – stores hostel and incharge details


**residents** – stores resident information

---

## 📂 Project Structure


HostelSphere-WebApp/

│

├───────── app.py

├── templates/

│       ├── index.html

│       ├── login.html

│       ├── register_hostel.html

│       ├── register_resident.html

│       ├── login_hostel.html

│       └── dashboard.html

├──────── static/

│     ├── css/

│     ├── images/

│     └── js/

└─────── README.md


---

## 🎯 Motivation


This project was built to solve real-world problems I experienced personally in hostel life, such as manual record keeping, lack of transparency, and inefficient hostel management.

## 🔮 Future Improvements


- Notice management system


- Fee tracking and payment status


- Improved UI using a frontend framework
  
- deployment


---

## 👤 Developed by sxumit
