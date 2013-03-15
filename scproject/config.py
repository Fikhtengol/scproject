import os
outer_dir=os.path.expanduser('./trekout')
if not  os.path.exists(outer_dir):
    try:
        os.makedirs(outer_dir)
    except:
        outer_dir = os.getcwd() 
        
