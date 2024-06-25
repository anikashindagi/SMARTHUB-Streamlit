import streamlit as st

def app():
    st.title("Contact Book welcomes you!")
    st.write("Save all your contacts here--")
    
    if 'contacts' not in st.session_state:
        st.session_state.contacts = []

    name = st.text_input("Enter the name:")
    phone = st.text_input("Enter the phone number:")
    email = st.text_input("Enter the email:")
    address = st.text_input("Enter the address:")
    
    if st.button("Add Contact"):
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        st.session_state.contacts.append(contact)
        st.success(f"Added contact: \nName: {name} Phn: {phone} Email: {email} Address: {address}")
    
    # Display the list of contacts
    st.write("Contacts:")
    if st.session_state.contacts:
        for i, contact in enumerate(st.session_state.contacts):
            st.write(f"{i+1}. Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']} | Address: {contact['address']}")
        
        contact_to_delete = st.number_input(
            "Enter the index of the contact to delete:", 
            min_value=1, 
            max_value=len(st.session_state.contacts), 
            step=1,
            key="contact_to_delete"
        )
        
        if st.button("Delete Contact"):
            if 1 <= contact_to_delete <= len(st.session_state.contacts):
                deleted_contact = st.session_state.contacts.pop(contact_to_delete - 1)
                st.success(f"Deleted contact: \nName: {deleted_contact['name']} Phn: {deleted_contact['phone']} Email: {deleted_contact['email']} Address: {deleted_contact['address']}")
            else:
                st.error("Invalid index")
    else:
        st.write("No contacts available to display.")
    
if __name__ == "__main__":
    app()
