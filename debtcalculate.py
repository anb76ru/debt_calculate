KV = """
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                        md_bg_color: 0, 0, 0, 1
                    
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        background_color: 0.1, 0.1, 0.1, 1
                    
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/font][/ref] Input"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    MDIconButton:
                                        icon: "calendar-month"
                                    
                                    MDTextField:
                                        id: start_date
                                        hint_text: 'Start date'
                                        #on_focus: if self.focus: app.date_dialog.open()
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        text_hint_color: 0,0,1,1
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cash"
                                        
                                    MDTextField:
                                        id: loan
                                        name: 'loan'
                                        hint_text: 'Loan'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"
                                
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "clock-time-five-outline"

                                    MDTextField:
                                        id: months
                                        name: 'months'
                                        hint_text: 'Months'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'int'
                                        helper_text_mode: "on_focus"
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "bank"

                                    MDTextField:
                                        id: interest
                                        name: 'interest'
                                        hint_text: 'Interest'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                    MDTextField:
                                        id: payment_type
                                        name: 'payment_type'
                                        hint_text: 'Payment type'
                                        text: "annuity"
                                        on_focus: if self.focus: app.menu.open()
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                
                                # BoxLayout:
                                #     MDIconButton:
                                #         icon: "account-group"
                                #     MDTextField:
                                #         id: participant_count
                                #         name: 'participant count'
                                #         hint_text: 'participant count'
                                # 
                                #     MyButton:
                                #         text: "create"
                                #         on_release: app.create_table_to_add_data()
                                        
                                        
                                
                                BoxLayout:
                                    spacing: "50"
                                    padding: 50
                                    MDList:
                                        id: scroll
                                    MDList:
                                        id: scroll2

                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/font][/ref] Table"
                            
                            BoxLayout:
                                orientation: 'vertical'

                                MDBoxLayout:
                                    padding: [20, 30, 20, 0]
                                    pos_hint: {"top": 1}
                                    adaptive_height: True
                                    
                                    MDIconButton:
                                        icon: "account-group"
                                    MDTextField:
                                        id: participant_count
                                        name: 'participant count'
                                        hint_text: 'participant count'
                                
                                    MyButton:
                                        text: "create"
                                        on_release: app.create_table_to_add_data()
                                
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: [20, 20, 25, 0]
                                    adaptive_height: True

                                    ScrollView:
                                        MDList:
                                            id: table_list
                                    
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: [20, 20, 20, 20]
                                    
                                    MDBoxLayout:
                                        # padding: [20, 20, 20, 20]

                                        MyButton: 
                                            text: 'add'
                                            on_release: app.add_row()

                                    MDBoxLayout:    
                                        # padding: [20, 20, 20, 20]

                                        MyButton: 
                                            text: 'remove'
                                            on_release: app.remove_row()
                                            
                                    MDBoxLayout:    
                                        # padding: [20, 20, 20, 20]

                                        MyButton: 
                                            text: 'calc'
                                            on_release: app.calc_debt()
                                    
                        
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/font][/ref] Graph"
                            
                            BoxLayout:
                                orientation: "vertical"
                        
                                ScrollView:
                        
                                    MDList:
                                        id: box
                            
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/font][/ref] Chart"
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/font][/ref] Sum"
    


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

<ItemColor>:
    size_hint_y: None
    height: "42dp"
    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos
            
    # MDLabel:
    #     text: root.text     
    #     halling: "center"   
    
    MDIconButton:
        icon: "account"    
    MyTextField:
        id: name
        name: 'name'
        
    MDIconButton:
        icon: "cash-multiple"   
    MDTextField:   
        id: expenses
        # name: 'expenses'
        # hint_text: 'expenses'
           
"""