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


def bt_dang8_p1_b1_c4_ds10(self):
            #Khai báo biến
            a = randint(-5,5)
            if a==0:
                a = randint(-5,5)
            b = randint(-5,5)
            c = randint(-5,5)
            x0 = randint(0,5)
            k1=randint(1,5)
            x1=x0+k1
            k2=randint(1,5)
            x2=x1+k2
            k3=randint(1,5)
            x3=x2+k3
            k4=randint(1,5)
            x4=x3+k4
            f1=x1**2/2
            f2=x2**2/2
            f3=x3**2/2
            f4=x4**2/2
            lis1=[x1,x2,x3,x4]
            lis2=[f1,f2,f3,f4]
            # Tạo một từ điển ánh xạ giữa giá trị x và giá trị f tương ứng
            mapping = dict(zip(lis1, lis2))
            bien=random.choice(lis1)
            ham = mapping[bien]
            #Nội dung câu hỏi
            noidungcauhoi = ('''Bảng sau cho biết nồng độ bụi PM $2zz5$ trong không khí theo thời gian trong ngày tại một trạm quan trắc của một địa phương \n''' 
                            "\\begin{center} \n"
                            "\\begin{tabular}{|c|>{\\centering\\arraybackslash}m{1cm}|>{\\centering\\arraybackslash}m{1cm}|>{\\centering\\arraybackslash}m{1cm}|>{\\centering\\arraybackslash}m{1cm}|} \n"
                            "\\hline \n"
                            "Thời điểm (giờ)& $%s$  & $%s$  & $%s$  & $%s$ \\\\ \n"
                            "\\hline \n"
                            "Nồng độ bụi PM $2zz5$ ($\\mu$g/m$^3)$ &$%s$ & $%s$  & $%s$  &$%s$  \\\\ \n"
                            "\\hline \n"
                            "\\end{tabular} \n"
                            "\\end{center} \n"
                            "Nồng độ bụi PM $2zz5$ tại thời điểm $%s$ giờ bằng \n"
                            %(latex(x1),latex(x2),latex(x3),latex(x4),
                            latex(f1),latex(f2),latex(f3),latex(f4),
                            latex(bien)
                            ))
            # Các đáp án
            if ham==f1:
                da_d = '\\True $%s$'%(latex(ham)) 
                da_s1 = '$%s$'%(latex(f2)) 
                da_s2 = '$%s$'%(latex(f3))  
                da_s3 = '$%s$'%(latex(f4)) 
            if ham==f2:
                da_d = '\\True $%s$'%(latex(ham)) 
                da_s1 = '$%s$'%(latex(f1)) 
                da_s2 = '$%s$'%(latex(f3))  
                da_s3 = '$%s$'%(latex(f4)) 
            if ham==f3:
                da_d = '\\True $%s$'%(latex(ham)) 
                da_s1 = '$%s$'%(latex(f2)) 
                da_s2 = '$%s$'%(latex(f1))  
                da_s3 = '$%s$'%(latex(f4)) 
            if ham==f4:
                da_d = '\\True $%s$'%(latex(ham)) 
                da_s1 = '$%s$'%(latex(f2)) 
                da_s2 = '$%s$'%(latex(f3))  
                da_s3 = '$%s$'%(latex(f1)) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=( 'Từ bảng giá trị ta có nồng độ bụi PM $2.5$ tại thời điểm $%s$ giờ bằng $%s$zz\\\\'
                    %(latex(bien),latex(ham))
                    )
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','').replace('\\frac','\\dfrac').replace('.',',').replace('zz','.')      
            return content

