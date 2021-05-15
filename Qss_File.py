def Qss():
    qss = '''
    QPushButton
    {
        background-color:#FFE4C4; /*背景色*/ 
        border-style:solid;
        border-width:2px;
        border-radius:5px; /*边界圆滑*/
        border-color:#F4A460;
        min-width:2em;
        color:black; /*字体颜色*/
        font-family:"宋体";
        text-align:center center;
        font-size: 12pt; /* 文本字体大小 */
        padding:2px
    }
    QPushButton:hover
    {
        background-color:#FFDAB9;
    }
    QPushButton:hover:pressed
    {
        background-color:#FFFACD;
    }
    QTabWidget::pane 
    { /* The tab widget frame */
        border-top: 2px solid #C2C7CB;
    }
    QTabWidget::tab-bar 
    {
        left: 5px; /* move to the right by 5px */
    }
    /* Style the tab using the tab sub-control. Note that
    it reads QTabBar _not_ QTabWidget */
    QTabBar::tab 
    {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
        stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
        border: 2px solid #C4C4C3;
        border-bottom-color: #C2C7CB; /* same as the pane color */
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        min-width: 8ex;
        padding: 2px;
    }
    QTabBar::tab:selected, QTabBar::tab:hover 
    {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #fafafa, stop: 0.4 #f4f4f4,
        stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
    }
    QTabBar::tab:selected 
    {
        border-color: #9B9B9B;
        border-bottom-color: #C2C7CB; /* same as pane color */
    }
    QTabBar::tab:!selected 
    {
        margin-top: 2px; /* make non-selected tabs look smaller */
    }
    /* make use of negative margins for overlapping tabs */
    QTabBar::tab:selected 
    {
        /* expand/overlap to the left and right by 4px */
        margin-left: -4px;
        margin-right: -4px;
    }
    QTabBar::tab:first:selected 
    {
        margin-left: 0; /* the first selected tab has nothing to overlap with on the left */
    }
    QTabBar::tab:last:selected 
    {
        margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
    }
    QTabBar::tab:only-one 
    {
        margin: 0; /* if there is only one tab, we don't want overlapping margins */
    }
    '''
    return qss