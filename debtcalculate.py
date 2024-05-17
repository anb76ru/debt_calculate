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
            source: "data/logo/money_payroll-photoaidcom-cropped.png"

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
            
            ItemDrawer
                id: info
                icon: "information-outline"
                text: "Информация"
                on_release: app.show_info()
            
            ItemDrawer:
                id: exit
                icon: "exit-to-app"
                text: "Выход"
                on_release: app.close_app()
    
    BoxLayout:
        pos_hint: {"bottom": 1}
        MDLabel:
            text: app.version
            font_style: "Caption"
            size_hint_y: None
            height: self.texture_size[1]


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
                        md_bg_color: 0.26, 0.40, 0.55, 1
                    
                    MDTabs:
                        id: tabs
                        background_color: 0.26, 0.40, 0.55, 1
                        allow_stretch: True
                        tab_display_mode: 'text'

                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=30][font={fonts[-1]['fn_regular']}]{md_icons['account-group']}[/font][/ref] Участники"

                            BoxLayout:
                                orientation: 'vertical'
                                pos_hint: {"top": 1}
                                adaptive_height: True
                                padding: [20, 30, 20, 0]
                                MDBoxLayout:
                                    pos_hint: {"top": 1}
                                    adaptive_height: True
                                    MDIconButton:
                                        icon: "account-multiple-plus"
                                        theme_text_color: "Custom"
                                        text_color: 0.26, 0.40, 0.55, 1
                                        
                                    MDTextField:
                                        id: participant_count
                                        name: 'participant count'
                                        hint_text: 'Количество'
                                        helper_text_mode: "on_focus"
                                        helper_text: 'max=99'
                                        max_text_length: 2
                                        line_color_focus: 0.26, 0.40, 0.55, 1
                                        input_filter: 'int'
                                    MyButton:
                                        text: "Создать таблицу"
                                        on_release: app.create_table_to_add_data()
                                        line_color: 0, 0, 0, 1
                                
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: [0, 20, 25, 80]
                                    adaptive_height: True

                                    ScrollView:
                                        MDList:
                                            id: table_list
                            
                            MDBoxLayout:      
                                orientation: 'horizontal'
                                padding: [20, 20, 20, 20]
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    MDBoxLayout:
                                        MyButton: 
                                            text: 'Добавить'
                                            on_release: app.add_row()
    
                                MDBoxLayout:    
                                    orientation: 'horizontal'
                                    MyButton: 
                                        text: 'Удалить'
                                        on_release: app.remove_row()

                                MDBoxLayout:    
                                    # padding: [20, 20, 20, 20]

                                    MyButton: 
                                        text: 'Рассчитать'
                                        on_release: app.calc_debt()
                                    
                        
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=30][font={fonts[-1]['fn_regular']}]{md_icons['account-cash']}[/font][/ref] Расчет"
                            BoxLayout:
                                orientation: 'vertical'
                                pos_hint: {"top": 1}
                                adaptive_height: True
                                padding: [20, 30, 20, 20]
                                MDBoxLayout:
                                    
                                    ScrollView:
                                        MDList:
                                            id: box
    
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
    
    MDIconButton:
        icon: "account"
        theme_text_color: "Custom"
        text_color: 0.26, 0.40, 0.55, 1    
    
    MyTextField:
        id: name
        name: 'name'
        
    MDIconButton:
        icon: "cash-multiple"   
        theme_text_color: "Custom"
        text_color: 0.26, 0.40, 0.55, 1

    MDTextField:   
        id: expenses
        input_filter: 'float'
        # name: 'expenses'
        # hint_text: 'expenses'

<InfoContent>        
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "400dp"

    ScrollView:
        
        MDList:
            padding: [20, 30, 20, 20]
            id: info_list

"""             