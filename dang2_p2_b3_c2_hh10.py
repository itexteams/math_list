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


def bt_dang2_p2_b3_c2_hh10(self):
        # Khai báo biến
        a1 = randint(2, 5)
        c1 = randint(2, 5)
        
        # ĐIỀU KIỆN BẮT BUỘC: Để 3 điểm M, N, P thẳng hàng thì 1/b = 1/a + 1/c => b1 = a1 + c1
        # Ta cố định b1 theo a1 và c1 thay vì random b1 bừa bãi
        b1 = a1 + c1

        a = Rational(1, a1)
        c = Rational(1, c1)
        b = Rational(1, b1)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ và các điểm $M, N, P$ thỏa mãn $\\vec{AM}=%s \\vec{AB}, \\vec{AN}=%s \\vec{AC}$ và $\\vec{AP}=%s \\vec{AD}$. \n'''
                        % (latex(a), latex(b), latex(c)))
        
        ######################################################################## Nhận biết 
        nb_da_d = '\\True $\\vec{AN}=%s \\left( \\vec{AB}+\\vec{AD} \\right)$' % (latex(b))
        nb_da_s = '$\\vec{AN}=%s \\left( \\vec{AB}+\\vec{AD} \\right)$' % (latex(b + Rational(1, 2))) 
        
        loigiai_nb = ('Ta có $\\vec{AC} = \\vec{AB} + \\vec{AD}$ (quy tắc hình bình hành). \\\\ \n'
                      'Suy ra $\\vec{AN}=%s \\vec{AC}=%s \\left( \\vec{AB}+\\vec{AD} \\right)$.'
                      % (latex(b), latex(b)))

        ######################################################################## Thông hiểu 
        th_da_d = '\\True $\\vec{MN}=%s \\vec{AB}+%s\\vec{AD}$' % (latex(b-a), latex(b))
        th_da_s = '$\\vec{MN}=%s \\vec{AB}+%s\\vec{AD}$' % (latex(a-b), latex(b)) # Đảo dấu để tạo nhiễu
        
        loigiai_th = ('Ta có $\\vec{MN}=\\vec{AN}-\\vec{AM}=%s \\left( \\vec{AB}+\\vec{AD} \\right)-%s \\vec{AB}=%s \\vec{AB}+%s\\vec{AD}$.'
                      % (latex(b), latex(a), latex(b-a), latex(b)))

        ######################################################################## Vận dụng 
        vd_da_d = '\\True $\\vec{MP}=%s \\vec{AD}-%s\\vec{AB}$' % (latex(c), latex(a))
        vd_da_s = '$\\vec{MP}=%s \\vec{AD}+%s\\vec{AB}$' % (latex(c), latex(a)) # Đổi - thành + để tạo nhiễu
        
        loigiai_vd = ('Ta có $\\vec{MP}=\\vec{AP}-\\vec{AM}=%s \\vec{AD}-%s\\vec{AB}$.'
                      % (latex(c), latex(a)))

        ######################################################################## Vận dụng cao 
        vdc_da_d = '\\True Ba điểm $M, N, P$ thẳng hàng'
        vdc_da_s = 'Ba điểm $M, N, P$ không thẳng hàng'
        
        # Chứng minh logic và thuyết phục hơn nhờ ràng buộc b1 = a1 + c1
        loigiai_vdc = ('Ta có $\\dfrac{1}{a} + \\dfrac{1}{c} = %s + %s = %s = \\dfrac{1}{b}$. \\\\ \n'
                       'Suy ra $\\dfrac{1}{b} - \\dfrac{1}{a} = \\dfrac{1}{c} \\Rightarrow \\dfrac{a-b}{ab} = \\dfrac{1}{c} \\Rightarrow b-a = -\\dfrac{ab}{c}$. \\\\ \n'
                       'Lại có $\\vec{MN}= %s \\vec{AB} + %s \\vec{AD} = -\\dfrac{ab}{c}\\vec{AB} + b\\vec{AD} = \\dfrac{b}{c}\\left(-a\\vec{AB} + c\\vec{AD}\\right) = %s\\vec{MP}$. \\\\ \n'
                       'Suy ra hai vectơ $\\vec{MN}$ và $\\vec{MP}$ cùng phương. Vậy ba điểm $M, N, P$ thẳng hàng.'
                       % (a1, c1, b1, latex(b-a), latex(b), latex(b/c)))

        # Vòng lặp đảm bảo số lượng câu đúng rơi vào khoảng 1 đến 3 (tránh trường hợp 4 True / 4 False)
        while True:
            nb_da = random.choice([nb_da_d, nb_da_s])
            th_da = random.choice([th_da_d, th_da_s])
            vd_da = random.choice([vd_da_d, vd_da_s])
            vdc_da = random.choice([vdc_da_d, vdc_da_s])
            
            true_count = sum('\\True' in ans for ans in [nb_da, th_da, vd_da, vdc_da])
            if 1 <= true_count <= 3:
                break

        # Xuất câu hỏi
        content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n'+ str(noidungcauhoi)+ 
            '\\choiceTFn \n'
            '{'+str(nb_da)+'}\n'
            '{'+str(th_da)+'}\n'
            '{'+str(vd_da)+'}\n'
            '{'+str(vdc_da)+'}\n'
            '\\loigiai{ \n'
            '\\begin{enumEX}[a)]{1} \n'
            '\\item '+str(loigiai_nb)+'\n'
            '\\item '+str(loigiai_th)+'\n'
            '\\item '+str(loigiai_vd)+'\n'
            '\\item '+str(loigiai_vdc)+'\n'
            '\\end{enumEX}} \n'
            '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
        
        return content 

