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


def bt_dang6_p1_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                a2=randint(-9,9)
                b2=randint(-9,9)
                c2=randint(-9,9)
                xa=randint(-9,9)
                ya=randint(-9,9)
                za=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)
                zb=randint(-9,9)


                while a1==0 or a2==0 or b1==0 or b2==0 or c1==0 or c2==0 or a1*a2+b1*b2+c1*c2!=0 :
                    a1=randint(-9,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)
                    a2=randint(-9,9)
                    b2=randint(-9,9)
                    c2=randint(-9,9)
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    za=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    zb=randint(-9,9)
                st=[1,2,3,4]
                random.shuffle(st)
                s1=st[0]
                s2=st[1]
                s3=st[2]
                s4=st[3]





                du = ['$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s1),latex(xb),latex(a2),latex(yb),latex(b2),latex(zb),latex(c2))
                    ]
                da= random.choice(du)
                s = ['$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s2),latex(xb+3),latex(a2),latex(yb+1),latex(b2),latex(zb-2),latex(-c2)),
                    '$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s3),latex(xb+1),latex(a2),latex(yb+2),latex(-b2),latex(zb+3),latex(c2)),
                    '$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s4),latex(xb),latex(-a2),latex(yb+4),latex(b2),latex(zb+1),latex(c2))


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('Trong không gian $Oxyz$, cho đường thẳng $\\Delta :\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$. Đường thẳng nào sau đây vuông góc với $\\Delta$'%(latex(xa),latex(a1),latex(ya),latex(b1),latex(za),latex(c1))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Các đường thẳng $\\Delta, \\Delta_%s$ tương ứng có các vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s),\\vec{u_2}=(%s;%s;%s)$.\\\\ \n'
                        'Do $\\vec{u_1}\\cdot\\vec{u_2}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=0$ nên $\\Delta \\perp \\Delta_%s$.'
                        %(latex(s1),latex(a1),latex(b1),latex(c1),
                            latex(a2),latex(b2),latex(c2),
                            latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),latex(s1),

                            )


                        )
            if dang=='2':
                # Khai báo biến
                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                a2=randint(-9,9)
                b2=randint(-9,9)
                c2=randint(-9,9)
                xa=randint(-9,9)
                ya=randint(-9,9)
                za=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)
                zb=randint(-9,9)


                while a1==0 or a2==0 or b1==0 or b2==0 or c1==0 or c2==0 or a1*a2+b1*b2+c1*c2!=0 :
                    a1=randint(-9,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)
                    a2=randint(-9,9)
                    b2=randint(-9,9)
                    c2=randint(-9,9)
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    za=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    zb=randint(-9,9)
                st=[1,2,3,4]
                random.shuffle(st)
                s1=st[0]
                s2=st[1]
                s3=st[2]
                s4=st[3]





                du = ['$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s1),latex(xb),latex(a2),latex(yb),latex(b2),latex(zb),latex(c2))
                    ]
                da= random.choice(du)
                s = ['$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s2),latex(xb+3),latex(a2),latex(yb+1),latex(b2),latex(zb-2),latex(-c2)),
                    '$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s3),latex(xb+1),latex(a2),latex(yb+2),latex(-b2),latex(zb+3),latex(c2)),
                    '$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s4),latex(xb),latex(-a2),latex(yb+4),latex(b2),latex(zb+1),latex(c2))


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('Trong không gian $Oxyz$, cho đường thẳng $\\Delta :\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$. Đường thẳng nào sau đây vuông góc với $\\Delta$'%(latex(xa),latex(a1),latex(ya),latex(b1),latex(za),latex(c1))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Các đường thẳng $\\Delta, \\Delta_%s$ tương ứng có các vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s),\\vec{u_2}=(%s;%s;%s)$.\\\\ \n'
                        'Do $\\vec{u_1}\\cdot\\vec{u_2}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=0$ nên $\\Delta \\perp \\Delta_%s$.'
                        %(latex(s1),latex(a1),latex(b1),latex(c1),
                            latex(a2),latex(b2),latex(c2),
                            latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),latex(s1),

                            )


                        )
            if dang=='3':
                # Khai báo biến
                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                a2=randint(-9,9)
                b2=randint(-9,9)
                c2=randint(-9,9)
                xa=randint(-9,9)
                ya=randint(-9,9)
                za=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)
                zb=randint(-9,9)


                while a1==0 or a2==0 or b1==0 or b2==0 or c1==0 or c2==0 or a1*a2+b1*b2+c1*c2!=0 :
                    a1=randint(-9,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)
                    a2=randint(-9,9)
                    b2=randint(-9,9)
                    c2=randint(-9,9)
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    za=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    zb=randint(-9,9)
                st=[1,2,3,4]
                random.shuffle(st)
                s1=st[0]
                s2=st[1]
                s3=st[2]
                s4=st[3]





                du = ['$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s1),latex(xb),latex(a2),latex(yb),latex(b2),latex(zb),latex(c2))
                    ]
                da= random.choice(du)
                s = ['$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s2),latex(xb+3),latex(a2),latex(yb+1),latex(b2),latex(zb-2),latex(-c2)),
                    '$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s3),latex(xb+1),latex(a2),latex(yb+2),latex(-b2),latex(zb+3),latex(c2)),
                    '$\\Delta_%s:\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$'%(latex(s4),latex(xb),latex(-a2),latex(yb+4),latex(b2),latex(zb+1),latex(c2))


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('Trong không gian $Oxyz$, cho đường thẳng $\\Delta :\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$. Đường thẳng nào sau đây vuông góc với $\\Delta$'%(latex(xa),latex(a1),latex(ya),latex(b1),latex(za),latex(c1))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Các đường thẳng $\\Delta, \\Delta_%s$ tương ứng có các vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s),\\vec{u_2}=(%s;%s;%s)$.\\\\ \n'
                        'Do $\\vec{u_1}\\cdot\\vec{u_2}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=0$ nên $\\Delta \\perp \\Delta_%s$.'
                        %(latex(s1),latex(a1),latex(b1),latex(c1),
                            latex(a2),latex(b2),latex(c2),
                            latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),latex(s1),

                            )


                        )

            if dang=='4':
                # Khai báo biến
                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)
                a2=randint(-9,9)
                b2=randint(-9,9)
                c2=randint(-9,9)
                xa=randint(-9,9)
                ya=randint(-9,9)
                za=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)
                zb=randint(-9,9)


                while a1==0 or a2==0 or b1==0 or b2==0 or c1==0 or c2==0 or a1*a2+b1*b2+c1*c2!=0 :
                    a1=randint(-9,9)
                    b1=randint(-9,9)
                    c1=randint(-9,9)
                    a2=randint(-9,9)
                    b2=randint(-9,9)
                    c2=randint(-9,9)
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    za=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    zb=randint(-9,9)
                st=[1,2,3,4]
                random.shuffle(st)
                s1=st[0]
                s2=st[1]
                s3=st[2]
                s4=st[3]





                du = ['$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s1),latex(xb),latex(a2),latex(yb),latex(b2),latex(zb),latex(c2))
                    ]
                da= random.choice(du)
                s = ['$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s2),latex(xb+3),latex(a2),latex(yb+1),latex(b2),latex(zb-2),latex(-c2)),
                    '$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s3),latex(xb+1),latex(a2),latex(yb+2),latex(-b2),latex(zb+3),latex(c2)),
                    '$\\Delta_%s:\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{z-%s}{%s}$'%(latex(s4),latex(xb),latex(-a2),latex(yb+4),latex(b2),latex(zb+1),latex(c2))


                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('Trong không gian $Oxyz$, cho đường thẳng $\\Delta :\\heva{&x=%s+%st\\\\&y=%s+%st\\\\&z=%s+%st}$. Đường thẳng nào sau đây vuông góc với $\\Delta$'%(latex(xa),latex(a1),latex(ya),latex(b1),latex(za),latex(c1))
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Các đường thẳng $\\Delta, \\Delta_%s$ tương ứng có các vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s),\\vec{u_2}=(%s;%s;%s)$.\\\\ \n'
                        'Do $\\vec{u_1}\\cdot\\vec{u_2}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=0$ nên $\\Delta \\perp \\Delta_%s$.'
                        %(latex(s1),latex(a1),latex(b1),latex(c1),
                            latex(a2),latex(b2),latex(c2),
                            latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),latex(s1),

                            )


                        )            

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+').replace('+-','-').replace('\\frac','\\dfrac').replace('+1t','+t').replace('-1t','-t').replace('x-0','x').replace('y-0','y').replace('z-0','z').replace('=0-','=-').replace('=0+','=+')
            return content

