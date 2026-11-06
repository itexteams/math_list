import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang3_p2_b1_c4_ds10(self):
            # Khai báo biến
            a=randint(1,9)

            # Nội dung câu hỏi
            noidungcauhoi = ('\\immini{'
                            'Cho hàm số $y=f(x)$ có đồ thị như hình vẽ với tỉ lệ trên các trục số là $%s$ đơn vị.'
                            '}{'
                            '''
                            \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
            \\scalebox{0.6}{ 
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-3.2108887271276165,-3.170822116415883) rectangle (5.19058372018441,4.180466274982139);
                    \\draw [samples=50,rotate around={-180.:(0.,2.)},xshift=0.cm,yshift=2.cm,line width=1.pt,color=ffqqqq,domain=-2.0:2.0)] plot (\\x,{(\\x)^2/2/0.5});
                    \\draw [line width=1.pt,color=ffqqqq] (2.,-2.)-- (4.,3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,4.)-- (5.,4.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,3.)-- (5.,3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,2.)-- (5.,2.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,1.)-- (5.,1.);
                    \\draw [line width=1.pt] (-3.,0.)-- (5.01055216774201,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,-1.)-- (5.,-1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,-2.)-- (5.,-2.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,-3.)-- (5.,-3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-2.,4.)-- (-2.,-3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-1.,4.)-- (-1.,-3.);
                    \\draw [line width=1.pt] (1.,4.)-- (1.,-3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,4.)-- (2.,-3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,4.)-- (3.,-3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (4.,4.)-- (4.,-3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (5.,4.)-- (5.,-3.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (-3.,4.)-- (-3.,-3.);
                    \\draw [->,line width=1.pt] (-3.,0.) -- (5.010552167742009,0.);
                    \\draw [->,line width=1.pt] (1.,-3.) -- (1.,4.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.009675711008660492,4.)-- (0.03968096974906077,-3.);
                    \\draw (0.4,0.059744074633860084) node[anchor=north west] {$O$};
                    \\draw (4.5,-0.1) node[anchor=north west] {$x$};
                    \\draw (0.5,4.0504434871070725) node[anchor=north west] {$y$};
            \\end{tikzpicture} }
                            '''
                            '}'

                            %(latex(a)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tập xác định của hàm số là $\\mathscr{D}=[%s; %s]$' %(latex(-3*a),latex(3*a))
            nb_da_1_s = 'Tập xác định của hàm số là $\\mathscr{D}=[%s; %s]$' %(latex(-3*a),latex(3*a+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Tập xác định của hàm số là $\\mathscr{D}=[%s; %s]$.' %(latex(-3*a),latex(3*a))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tập giá trị của hàm số là $[%s;%s]$' %(latex(-2*a),latex(3*a))  
            th_da_1_s = 'Tập giá trị của hàm số là $[%s;%s]$' %(latex(-2*a-1),latex(3*a))  
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Giá trị lớn nhất của hàm số là $%s$' %(latex(3*a))
            th_da_2_s = 'Giá trị lớn nhất của hàm số là $%s$' %(latex(3*a+1)) 
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True Giá trị nhỏ nhất của hàm số là $%s$' %(latex(-2*a))  
            th_da_3_s = 'Giá trị nhỏ nhất của hàm số là $%s$' %(latex(-2*a+1)) 
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2,th_da_3]

            # Nội dung lời giải
            loigiai_th_1 = ('Tập giá trị của hàm số là $[%s;%s]$.' %(latex(-2*a),latex(3*a))           
                        )
            loigiai_th_2 = ('Giá trị lớn nhất của hàm số là $%s$.' %(latex(3*a))           
                        )
            loigiai_th_3 = ('Giá trị nhỏ nhất của hàm số là $%s$.' %(latex(-2*a))           
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2,loigiai_th_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Đồ thị hàm số đi qua điểm $(%s;%s)$' %(latex(-3*a),latex(-2*a))  
            vd_da_1_s = 'Đồ thị hàm số không đi qua điểm $(%s;%s)$' %(latex(-3*a),latex(-2*a))  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Đồ thị hàm số đi qua điểm $(%s;%s)$' %(latex(-2*a),latex(a))  
            vd_da_2_s = 'Đồ thị hàm số không đi qua điểm $(%s;%s)$' %(latex(-2*a),latex(a))  
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True Đồ thị hàm số đi qua điểm $(%s;%s)$' %(latex(-a),latex(2*a))  
            vd_da_3_s = 'Đồ thị hàm số không đi qua điểm $(%s;%s)$' %(latex(-a),latex(2*a))  
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            vd_da_4_d = '\\True Đồ thị hàm số đi qua điểm $(0;%s)$' %(latex(a))  
            vd_da_4_s = 'Đồ thị hàm số không đi qua điểm $(0;%s)$' %(latex(a))  
            list_vd_da_4=[vd_da_4_d,vd_da_4_s]
            vd_da_4=random.choice(list_vd_da_4)

            vd_da_5_d = '\\True Đồ thị hàm số đi qua điểm $(%s;%s)$' %(latex(a),latex(-2*a))  
            vd_da_5_s = 'Đồ thị hàm số không đi qua điểm $(%s;%s)$' %(latex(a),latex(-2*a))  
            list_vd_da_5=[vd_da_5_d,vd_da_5_s]
            vd_da_5=random.choice(list_vd_da_5)

            vd_da_6_d = '\\True Đồ thị hàm số đi qua điểm $(%s;%s)$' %(latex(3*a),latex(4*a))  
            vd_da_6_s = 'Đồ thị hàm số không đi qua điểm $(%s;%s)$' %(latex(3*a),latex(4*a))  
            list_vd_da_6=[vd_da_6_d,vd_da_6_s]
            vd_da_6=random.choice(list_vd_da_6)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2,vd_da_3,vd_da_4,vd_da_5,vd_da_6]

            # Nội dung lời giải
            loigiai_vd_1 = ('Đồ thị hàm số đi qua điểm $(%s;%s)$.'%(latex(-3*a),latex(-2*a))   
                        )
            loigiai_vd_2 = ('Đồ thị hàm số đi qua điểm $(%s;%s)$.'%(latex(-2*a),latex(a))  
                        )
            loigiai_vd_3 = ('Đồ thị hàm số đi qua điểm $(%s;%s)$.'%(latex(-a),latex(2*a))  
                        )
            loigiai_vd_4 = ('Đồ thị hàm số đi qua điểm $(0;%s)$.'%(latex(a))  
                        )
            loigiai_vd_5 = ('Đồ thị hàm số đi qua điểm $(%s;%s)$.'%(latex(a),latex(-2*a))  
                        )
            loigiai_vd_6 = ('Đồ thị hàm số đi qua điểm $(%s;%s)$.'%(latex(3*a),latex(4*a))  
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3,loigiai_vd_4,loigiai_vd_5,loigiai_vd_6]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Hàm số đồng biến trên khoảng $(%s;%s)$' %(latex(-3*a),latex(-a)) 
            vdc_da_1_s = 'Hàm số đồng biến trên khoảng $(%s;%s)$' %(latex(-3*a),latex(-a+1)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Hàm số đồng biến trên khoảng $(%s;%s)$' %(latex(a),latex(3*a)) 
            vdc_da_2_s = 'Hàm số đồng biến trên khoảng $(%s;%s)$' %(latex(a-1),latex(3*a)) 
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True Hàm số nghịch biến trên khoảng $(%s;%s)$' %(latex(-a),latex(a)) 
            vdc_da_3_s = 'Hàm số nghịch biến trên khoảng $(%s;%s)$' %(latex(-a),latex(a+1)) 
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2,vdc_da_3]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Hàm số đồng biến trên khoảng $(%s;%s)$.' %(latex(-3*a),latex(-a)) 
                        )
            loigiai_vdc_2 = ('Hàm số đồng biến trên khoảng $(%s;%s)$.' %(latex(a),latex(3*a)) 
                        )
            loigiai_vdc_3 = ('Hàm số nghịch biến trên khoảng $(%s;%s)$.' %(latex(-a),latex(a)) 
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

