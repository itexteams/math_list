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


def bt_dang13_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Dữ liệu cố định từ đề bài hoặc có thể random nhẹ
            xA, yA = -1, 0
            xB, yB = 1, 2

            # Tính toán các đại lượng liên quan
            # 1. Vectơ AB và độ dài AB
            vecAB = (xB - xA, yB - yA) # (2, 2)
            AB2 = vecAB[0]**2 + vecAB[1]**2 # 8

            # 2. Phương trình đường thẳng AB: (yB-yA)(x-xA) - (xB-xA)(y-yA) = 0
            # 2(x + 1) - 2(y - 0) = 0 <=> x - y + 1 = 0
            ptAB = x - y + 1

            # 3. Phương trình đường thẳng BC (qua B và vuông góc AB)
            # Vectơ pháp tuyến là vecAB = (2, 2) -> x + y - 3 = 0
            ptBC = (x - xB) + (y - yB)

            # 4. Tìm tọa độ C (x; y) sao cho C thuộc BC và BC^2 = AB^2
            # y = 3 - x. Thay vào (x-1)^2 + (y-2)^2 = 8 => (x-1)^2 + (1-x)^2 = 8 => 2(x-1)^2 = 8 => x-1 = 2 hoặc -2
            # xC = 3 (hoành độ dương) => yC = 0. Vậy C(3; 0)
            xC, yC = 3, 0

            # 5. Tâm hình vuông I là trung điểm AC
            xI, yI = (xA + xC)/2, (yA + yC)/2 # (1, 0)

            # 6. Đường trung bình song song AB, CD
            # Đường thẳng CD qua C(3,0) song song AB: (x-3) - (y-0) = 0 <=> x - y - 3 = 0
            # Đường trung bình nằm giữa AB (x-y+1=0) và CD (x-y-3=0) là: x - y + (1-3)/2 = 0 <=> x - y - 1 = 0
            pt_mid = x - y - 1

            noidungcauhoi = ('''Trong mặt phẳng $Oxy$, cho hình vuông $ABCD$ có $A(%s; %s)$ và $B(%s; %s)$.''' 
                             %(latex(xA), latex(yA), latex(xB), latex(yB)))

            ########################################################################
            # Nhận biết: Phương trình BC
            nb_da_1_d = 'Phương trình đường thẳng $BC$ là $x + y - 3 = 0$'
            nb_da_1_s = 'Phương trình đường thẳng $BC$ là $x - y + 1 = 0$' # Thực chất là đường AB
            list_nb_da_1 = ['\\True ' + nb_da_1_d if random.choice([True, False]) else nb_da_1_s]
            if 'x - y + 1 = 0' in list_nb_da_1[0]:
                loigiai_nb_1 = 'Vectơ $\\vec{AB} = (%s; %s)$. Đường thẳng $BC$ đi qua $B(%s; %s)$ và vuông góc với $AB$ nên nhận $\\vec{AB}$ làm VTPT. Phương trình $BC: 1(x-1) + 1(y-2)=0 \\Leftrightarrow x+y-3=0$. Mệnh đề sai.' % (latex(vecAB[0]), latex(vecAB[1]), latex(xB), latex(yB))
            else:
                loigiai_nb_1 = 'Vectơ $\\vec{AB} = (%s; %s)$. Đường thẳng $BC$ đi qua $B(%s; %s)$ và vuông góc với $AB$ nên nhận $\\vec{AB}$ làm VTPT. Phương trình $BC: 1(x-1) + 1(y-2)=0 \\Leftrightarrow x+y-3=0$. Mệnh đề đúng.' % (latex(vecAB[0]), latex(vecAB[1]), latex(xB), latex(yB))

            list_nb_1 = [list_nb_da_1[0]]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Tọa độ điểm C
            th_da_1_d = 'Toạ độ của điểm $C$ có hoành độ dương là $(3; 0)$'
            th_da_1_s = 'Toạ độ của điểm $C$ có hoành độ dương là $(3; 4)$'
            choice_th = random.choice([True, False])
            th_da_1 = '\\True ' + th_da_1_d if choice_th else th_da_1_s

            loigiai_th_1 = ('''Điểm $C$ nằm trên đường thẳng $BC$ nên $C(t; 3-t)$. \\\\
                            Ta có $BC^2 = AB^2 = 8 \\Leftrightarrow (t-1)^2 + (3-t-2)^2 = 8 \\Leftrightarrow 2(t-1)^2 = 8$. \\\\
                            Giải ra $t=3$ hoặc $t=-1$. Vì hoành độ dương nên $C(3; 0)$.''')

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Tâm hình vuông
            vd_da_1_d = 'Toạ độ của tâm hình vuông $ABCD$ là $(1; 0)$'
            vd_da_1_s = 'Toạ độ của tâm hình vuông $ABCD$ là $(0; 1)$'
            choice_vd = random.choice([True, False])
            vd_da_1 = '\\True ' + vd_da_1_d if choice_vd else vd_da_1_s

            loigiai_vd_1 = 'Tâm $I$ của hình vuông là trung điểm của đoạn thẳng $AC$. Với $A(-1; 0)$ và $C(3; 0)$. \\\\ Ta có $I\\left(\\frac{-1+3}{2}; \\frac{0+0}{2}\\right) = (1; 0)$.'

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Đường trung bình
            vdc_da_1_d = 'Phương trình đường trung bình song song với 2 cạnh $AB$ và $CD$ là $x - y - 1 = 0$'
            vdc_da_1_s = 'Phương trình đường trung bình song song với 2 cạnh $AB$ và $CD$ là $x - y + 1 = 0$'
            choice_vdc = random.choice([True, False])
            vdc_da_1 = '\\True ' + vdc_da_1_d if choice_vdc else vdc_da_1_s

            loigiai_vdc_1 = ('''Đường thẳng $AB$ có phương trình $x-y+1=0$. \\\\
                             Đường thẳng $CD$ đi qua $C(3;0)$ và song song với $AB$ nên có phương trình $x-y-3=0$. \\\\
                             Đường trung bình song song với $AB, CD$ sẽ cách đều hai đường thẳng này, có phương trình: $x-y + \\frac{1+(-3)}{2} = 0 \\Leftrightarrow x-y-1=0$.''')

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp và xáo trộn theo mẫu
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Do mỗi phần chỉ có 1 câu nên shuffle ở đây chủ yếu để đúng cấu trúc mẫu
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

