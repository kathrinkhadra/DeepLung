config = {'train_data_path':['../../lunadata/subset0/subset0/',
                             '../../lunadata/subset1/subset1/',
                             '../../lunadata/subset2/subset2/',
                             '../../lunadata/subset3/subset3/'],
          'val_data_path':['../../lunadata/subset4/subset4/'], 
          'test_data_path':['../../lunadata/subset4/subset4/'], 
          
          'train_preprocess_result_path':'../../preprocess/',
          'val_preprocess_result_path':'../../preprocess/',  
          'test_preprocess_result_path':'../../preprocess/',
          
          'train_annos_path':'../../lunadata/annotations.csv',
          'val_annos_path':'../../lunadata/annotations.csv',
          'test_annos_path':'../../lunadata/annotations.csv',

          'black_list':[],
          
          'preprocessing_backend':'python',

          'luna_segment':'../../lunadata/seg-lungs-LUNA16/seg-lungs-LUNA16/',
          'preprocess_result_path':'../../preprocess/',
          'luna_data':'../../lunadata/',
          'luna_label':'../../lunadata/annotations.csv'
         } 
#../../ entfernen for preprocessing