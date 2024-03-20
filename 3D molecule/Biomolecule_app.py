import streamlit as st 
from st_speckmol import speck_plot
import glob
import os

def main():
    # tempdir=r"C:\Users\NEERA KUMARI\Desktop\New folder (4)\3D molecule"
    # def save_upload_file(Uploaded_file):
        
    #     with open(os.path.join(tempdir,Uploaded_file.name),"wb") as f:
    #         f.write((Uploaded_file.getbuffer()))
    #     return st.success(f"The file {Uploaded_file.name} has been saved")
    st.markdown(""" 
                ## Molecules 3D Visualization App
                 Streamlit web app for visualizing 3D models of biomolecules.
                 It showcases the 3D model of the molecule which you can explore effortlessly .
                 
                """)
    
    # st.sidebar.header("Select a File or Drop a File ")
    
    # st.button("")
     
    files=glob.glob("*.txt")
  
    
    with st.sidebar:
       
            
               
        chosen_file=st.selectbox("Choose files from the directory",files)
             
        file_reader=open(chosen_file,"r")
        coordinates_of_molecules=file_reader.read()    
       
        
        with st.sidebar.expander("Parameters",expanded=True):
            outl=st.checkbox("Outline",value=True)
            bond=st.checkbox("Bond",value=True)
            bond_scale=st.slider("Bond_Scale",min_value=0.0,max_value=1.0,value=0.6)
            Brightness=st.slider("Brightness",min_value=0.0,max_value=1.0,value=0.3)
            Rel_Atomic_Scale=st.slider("Relative Atomic Scale",min_value=0.0,max_value=1.0,value=0.8)
            Bond_Shade=st.slider("Bond_Shade",min_value=0.0,max_value=1.0,value=0.64)
            
            
        
        parameters={"outline":outl,"bondScale":bond_scale,"bondShade":Bond_Shade,"relativeAtomicScale":Rel_Atomic_Scale,"brightness":Brightness,"bonds":bond}
    
    
    
    # file=st.file_uploader("Upload File")
    # if file is not None:
    #     file_details={"file_name":file.name,"file_type":file.type,"file_size":file.size}
    #     st.write(file_details)
    #     st.write(str(file.read(),"utf-8"))
    #     save_upload_file(file)
        
    speck_plot(coordinates_of_molecules,wbox_height="500px",wbox_width="500px",_PARAMETERS=parameters)

        
        
       
       
    
    
    
    
    
    
    
    
    
    


if __name__=="__main__":
    main()