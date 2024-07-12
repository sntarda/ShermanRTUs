import streamlit as st
import pandas as pd

# Load data (assuming data is stored in a CSV file)
data_path = 'data/units_data.csv'

@st.cache
def load_data(path):
    return pd.read_csv(path)

df = load_data(data_path)

def building_1001():
    st.title('Building 1001')

    # Sidebar navigation
    if st.sidebar.button("Home/Dashboard"):
        st.experimental_rerun()
    if st.sidebar.button("Add/Edit Unit"):
        add_edit_unit(df)
    if st.sidebar.button("Add Ticket"):
        add_ticket(df)
    
    # Display AC units in Building 1001
    if 'Building' in df.columns:
        building_1001_units = df[df['Building'] == 1001]
        st.write("## AC Units in Building 1001")
        st.dataframe(building_1001_units)

        # Display details for a selected unit
        unit_ids = building_1001_units['RTU'].tolist()
        selected_unit = st.selectbox("Select an AC Unit", unit_ids, key="unit_select")
        if selected_unit:
            unit_details = building_1001_units[building_1001_units['RTU'] == selected_unit].iloc[0]
            st.write(f"### Details for Unit {selected_unit}")
            st.write(unit_details.to_dict())
    else:
        st.error("The 'Building' column is missing in the data.")

def add_edit_unit(df):
    st.write("### Add/Edit Unit")
    
    # Form to add or edit a unit
    with st.form(key='unit_form'):
        rtu = st.text_input("RTU", key="rtu")
        building = st.text_input("Building", key="building")
        suite = st.text_input("Suite", key="suite")
        manufacturer = st.text_input("Manufacturer", key="manufacturer")
        year = st.number_input("Year", min_value=1900, max_value=2100, step=1, key="year")
        model = st.text_input("Model", key="model")
        serial = st.text_input("Serial", key="serial")
        compressor_charge = st.text_input("Compressor Charge", key="compressor_charge")
        tonnage = st.number_input("Tonnage", min_value=0.0, step=0.1, key="tonnage")
        seer = st.number_input("SEER", min_value=0.0, step=0.1, key="seer")
        eer = st.number_input("EER", min_value=0.0, step=0.1, key="eer")
        heat = st.text_input("Heat", key="heat")
        heating_element = st.text_input("Heating Element", key="heating_element")
        power_supply = st.text_input("Power Supply", key="power_supply")
        routine_service = st.date_input("Routine Service", key="routine_service")
        status = st.selectbox("Status", ["Operational", "Repair Required", "Off", "Standby", "Due for Service", "Decommissioned", "Testing"], key="status")
        
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
        df.to_csv(data_path, index=False)  # Save updated dataframe to CSV
        st.success("Unit added/updated successfully")

def add_ticket(df):
    st.write("### Add Ticket")
    
    # Form to add a ticket
    with st.form(key='ticket_form'):
        rtu = st.text_input("RTU", key="ticket_rtu")
        date_requested = st.date_input("Date Requested", key="date_requested")
        issue = st.text_area("Issue", key="issue")
        date_checked = st.date_input("Date Checked", key="date_checked")
        tech_notes = st.text_area("Tech Notes", key="tech_notes")
        repair_status = st.selectbox("Repair Status", ["Complete", "Pending"], key="repair_status")
        date_repaired = st.date_input("Date Repaired", key="date_repaired")
        cost = st.number_input("Cost", min_value=0.0, step=0.1, key="cost")
        
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
        tickets_path = 'data/tickets.csv'
        try:
            tickets_df = pd.read_csv(tickets_path)
        except FileNotFoundError:
            tickets_df = pd.DataFrame(columns=["RTU", "Date Requested", "Issue", "Date Checked", "Tech Notes", "Repair Status", "Date Repaired", "Cost"])
        tickets_df = tickets_df.append(new_ticket, ignore_index=True)
        tickets_df.to_csv(tickets_path, index=False)  # Save updated dataframe to CSV
        st.success("Ticket added successfully")

building_1001()
