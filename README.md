# kivy_lottie_widget
How to render a lottie animation in kivy, took me alot of trial and error, its still a work in progress. This works in windows and linux most likely. I need someone to help me make this functional in ARM64(Android).

I have tried to use the ARM64 wheel available in the aarch64 wheel available here https://pypi.org/project/rlottie-python/#files, but failed I couldn't get the wheel to install in buildozer. When i built the app in buildozer with the regular r_lottie in requirements, the lottie app fails to run because the r_lottie installed is not aarch64, i went as far as to install the C binaries needed to run r_lottie but i couldn't get the binaries to work together correctly, i had some index error with one c binary and i gave up. If someone more experienced with kivy, or knows how to build the aarch whl for rlottie could help me out, it would be greatly appreciated.
This way Kivy could have finally have a lottie widget finally available for android development. 

The current version of how it is now, works in windows and most likely in linux also(haven't tested).

To use:
1.) install all that is in requirements.txt 
2.) run main.py
3.) You can test with any .json lottie, in this repo i used account.json.


🥖 _-_  




                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                         ..:::::..                                        
                                       .-----------.                                      
                                      .-------------.                                     
                                     .--------------:                                     
                                     .:-------------:                                     
                                      .--------------..                                   
                                      .--------------.                                    
                                      .--------------      :----:                         
                                      .--------------     --------.                       
                                      :--------------    :---------                       
                          .::-:.     .:--------------    -----------.                     
                                                                                          
                         :-.          .:                              :.                  
      =*****+-           =+:          +*.   .******+:                :*-                  
      =*-   -*+  -++++:  -=. =-=++-  =**+==:.**   .+*- .=+*+=. =:===::*=  -=: :=====-     
      =*-   :*+ +*:..=*+ =*: **-.:** .**-:: .**    +*=:*+:-*+. **=::.:*-.+*: .**---:.     
      =*++++*+..*+    ** =*: **.  =*. +*.   .**+++**- -*-=*-   **.   :****+.  -+****=     
      =*=::.    -*+--+*: +*: **.  =*. :*+==..**:::.    +**==*- **.   :**::**..=====**     
      ::.        .:--:   ::. ::   ::    .::. ::         .:-:.  ::    .:.  .:: ::::::      
                                                                                          
                        :----------------------------....                                 
                         .--------------------------:                                     
                           .:------------------------.                                    
                                ....:::--------------.                                    
                                      .-------------:                                     
                                      .-------------:                                     
                                     :--------------:                                     
                                      .--------------:.                                   
                                      .-------------:                                     
                                      .-------------:                                     
                                        ..:::::::..                                       
                                                                                          
                                                                                          
                                                                                          
