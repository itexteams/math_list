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


def bt_dang21_p1_b1_c2_hh12(self):
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-8,8)
                ya=randint(-8,8)
                za=randint(-5,5)
                while za==0:
                    x,y,z=symbols('x,y,z')
                    xa=randint(-8,8)
                    ya=randint(-8,8)
                    za=randint(-5,5)
                pt=z-za

                du = ['$%s=0$'%(latex(pt))
                    ]
                da= random.choice(du)
                s = ['$%s=0$'%(latex(pt+x)),
                    '$%s=0$'%(latex(pt+y)),
                    '$%s=0$'%(latex(pt+z)),
                    '$%s=0$'%(latex(pt+3)),
                    '$%s=0$'%(latex(pt+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, phương trình mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và song song với mặt phẳng $(Oxy)$ là '
                                %(latex(xa),latex(ya),latex(za)))



                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì mặt phẳng $(\\alpha)$ song song với $(Oxy)$, suy ra $(\\alpha)$ có một vectơ pháp tuyến là '
                        '$\\vec{n}=(0;0;1).$\\\\ \n'
                        'Mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và nhận $\\vec{n}=(0;0;1)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$0(x-%s)+0(y-%s)+1(z-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy phương trình mặt phẳng $(\\alpha)$ là $%s=0$.'

                        %(latex(xa),latex(ya),latex(za),
                        latex(xa),latex(ya),latex(za),
                        latex(pt),latex(pt)


                        )
                        )
            if dang=='2':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-8,8)
                ya=randint(-8,8)
                za=randint(-5,5)
                while xa==0:
                    x,y,z=symbols('x,y,z')
                    xa=randint(-8,8)
                    ya=randint(-8,8)
                    za=randint(-5,5)
                pt=x-xa

                du = ['$%s=0$'%(latex(pt))
                    ]
                da= random.choice(du)
                s = ['$%s=0$'%(latex(pt+x)),
                    '$%s=0$'%(latex(pt+y)),
                    '$%s=0$'%(latex(pt+z)),
                    '$%s=0$'%(latex(pt+3)),
                    '$%s=0$'%(latex(pt+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, phương trình mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và song song với mặt phẳng $(Oyz)$ là '
                                %(latex(xa),latex(ya),latex(za)))



                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì mặt phẳng $(\\alpha)$ song song với $(Oyz)$, suy ra $(\\alpha)$ có một vectơ pháp tuyến là '
                        '$\\vec{n}=(1;0;0).$\\\\ \n'
                        'Mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và nhận $\\vec{n}=(1;0;0)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$1(x-%s)+0(y-%s)+0(z-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy phương trình mặt phẳng $(\\alpha)$ là $%s=0$.'

                        %(latex(xa),latex(ya),latex(za),
                        latex(xa),latex(ya),latex(za),
                        latex(pt),latex(pt)


                        )
                        )
            if dang=='3':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                xa=randint(-8,8)
                ya=randint(-8,8)
                za=randint(-5,5)
                while ya==0:
                    x,y,z=symbols('x,y,z')
                    xa=randint(-8,8)
                    ya=randint(-8,8)
                    za=randint(-5,5)
                pt=y-ya

                du = ['$%s=0$'%(latex(pt))
                    ]
                da= random.choice(du)
                s = ['$%s=0$'%(latex(pt+x)),
                    '$%s=0$'%(latex(pt+y)),
                    '$%s=0$'%(latex(pt+z)),
                    '$%s=0$'%(latex(pt+3)),
                    '$%s=0$'%(latex(pt+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, phương trình mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và song song với mặt phẳng $(Oxz)$ là '
                                %(latex(xa),latex(ya),latex(za)))



                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì mặt phẳng $(\\alpha)$ song song với $(Oxz)$, suy ra $(\\alpha)$ có một vectơ pháp tuyến là '
                        '$\\vec{n}=(0;1;0).$\\\\ \n'
                        'Mặt phẳng $(\\alpha)$ đi qua điểm $A(%s;%s;%s)$ và nhận $\\vec{n}=(0;1;0)$ làm một vectơ pháp tuyến nên có phương trình là\\\\ \n'
                        '\\hspace*{1cm}$0(x-%s)+1(y-%s)+0(z-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                        'Vậy phương trình mặt phẳng $(\\alpha)$ là $%s=0$.'

                        %(latex(xa),latex(ya),latex(za),
                        latex(xa),latex(ya),latex(za),
                        latex(pt),latex(pt)


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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-').replace('+1\\cdot','+').replace('+-','-').replace('-1\\cdot','-').replace('$$1\\cdot','').replace('$$-1\\cdot','-')
            return content

