
import streamlit as st
import pandas as pd

# Load data (assuming data is stored in an Excel file)
data_path = 'data/units_data.csv'
df = pd.read_excel(data_path)

def building_1057():
    st.title('Building 1057')

    # Sidebar navigation
    if st.sidebar.button("Home/Dashboard"):
        st.experimental_rerun()
    if st.sidebar.button("Add/Edit Unit"):
        add_edit_unit()
    if st.sidebar.button("Add Ticket"):
        add_ticket()
    
    # Display AC units in Building 1057
    building_1057_units = df[df['Building'] == 1057]
    st.write("## AC Units in Building 1057")
    st.dataframe(building_1059_units)

    # Display details for a selected unit
    unit_ids = building_1057_units['RTU'].tolist()
    selected_unit = st.selectbox("Select an AC Unit", unit_ids)
    if selected_unit:
        unit_details = building_1057_units[building_1057_units['RTU'] == selected_unit].iloc[0]
        st.write(f"### Details for Unit {selected_unit}")
        st.write(unit_details.to_dict())

def add_edit_unit(df):
    st.write("### Add/Edit Unit")
    
    # Form to add or edit a unit
    with st.form(key='unit_form'):
        rtu = st.text_input("RTU")
        building = st.text_input("Building")
        suite = st.text_input("Suite")
        manufacturer = st.text_input("Manufacturer")
        year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
        model = st.text_input("Model")
        serial = st.text_input("Serial")
        compressor_charge = st.text_input("Compressor Charge")
        tonnage = st.number_input("Tonnage", min_value=0.0, step=0.1)
        seer = st.number_input("SEER", min_value=0.0, step=0.1)
        eer = st.number_input("EER", min_value=0.0, step=0.1)
        heat = st.text_input("Heat")
        heating_element = st.text_input("Heating Element")
        power_supply = st.text_input("Power Supply")
        routine_service = st.date_input("Routine Service")
        status = st.selectbox("Status", ["Operational", "Repair Required", "Off", "Standby", "Due for Service", "Decommissioned", "Testing"])
        
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        new_unit = {
            "RTU": rtu,
            "Building": building,
            "Suite": suite,
            "Manufacturer": manufacturer,
            "Year": year,
            "Model": model,
            "Serial": serial,
            "Compressor Charge": compressor_charge,
            "Tonnage": tonnage,
            "SEER": seer,
            "EER": eer,
            "Heat": heat,
            "Heating Element": heating_element,
            "Power Supply": power_supply,
            "Routine Service": routine_service,
            "Status": status
        }
        df = df.append(new_unit, ignore_index=True)
        df.to_excel('data/units_data.csv', index=False)  # Save updated dataframe to Excel
        st.success("Unit added/updated successfully")
      
def add_ticket(df):
    st.write("### Add Ticket")
    
    # Form to add a ticket
    with st.form(key='ticket_form'):
        rtu = st.text_input("RTU")
        date_requested = st.date_input("Date Requested")
        issue = st.text_area("Issue")
        date_checked = st.date_input("Date Checked")
        tech_notes = st.text_area("Tech Notes")
        repair_status = st.selectbox("Repair Status", ["Complete", "Pending"])
        date_repaired = st.date_input("Date Repaired")
        cost = st.number_input("Cost", min_value=0.0, step=0.1)
        
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        new_ticket = {
            "RTU": rtu,
            "Date Requested": date_requested,
            "Issue": issue,
            "Date Checked": date_checked,
            "Tech Notes": tech_notes,
            "Repair Status": repair_status,
            "Date Repaired": date_repaired,
            "Cost": cost
        }
        # Assuming there's a separate sheet or section for tickets
        tickets_df = pd.read_excel('data/units_data.csv', sheet_name='Tickets')
        tickets_df = tickets_df.append(new_ticket, ignore_index=True)
        tickets_df.to_excel('data/units_data.csv', sheet_name='Tickets', index=False)  # Save updated dataframe to Excel
        st.success("Ticket added successfully")

building_1057()
