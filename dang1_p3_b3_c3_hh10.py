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


def bt_dang1_p3_b3_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x = symbols("x")
                y = symbols('y')

                k = randint(1,5)
                r = 5*k
                hs1_1 = [3*k,4*k]
                hs1 = random.choice(hs1_1)
                if hs1==3*k:
                    hs2=4*k
                else:
                    hs2=3*k


                #Tọa độ điểm A
                a = randint(-9,9)   
                b = randint(-9,9)  
                c = a**2+b**2-r**2

                x_a = hs1+a
                y_a = hs2+b
                #Tọa độ điểm B
                x_b = -hs1+a
                y_b = -hs2+b
                #Tọa độ điểm C
                x_c = hs1+a
                y_c = -hs2+b

                pt = Eq((x-a)**2+(y-b)**2,r**2)
                pt1 = Eq((x+a)**2+(y+b)**2,r)
                pt2 = Eq((x-a)**2-(y-b)**2,r**2)
                pt3 = Eq((x+a)**2-(y+b)**2,r)

                # Câu hỏi
                noidungcauhoi='''Trong mặt phẳng tọa độ $(Oxy)$, cho ba điểm $A(%s;%s), B(%s;%s), C(%s;%s)$. Phương trình đường tròn đi qua ba điểm $A,B,C$ có tâm $I(a;b)$. Tổng $a+b$ bằng bao nhiêu?''' %(latex(x_a), latex(y_a), latex(x_b), latex(y_b), latex(x_c), latex(y_c))

                # Nội dung lời giải
                loigiai=( 'Giả sử phương trình đường tròn đi qua ba điểm có dạng  \\\\ '
                        '$x^2+y^2-2ax-2by+c=0$ với $a^2+b^2-c>0$ \\\\'
                        'Vì đường tròn đi qua ba điểm $A, B, C$ nên tọa độ ba điểm sẽ thỏa mãn phương trình đường tròn. \\\\ '
                        'Ta có hệ phương trình \\\\'
                        '$\\heva{& %s+%s-%s a -%s b+c=0 \\\\ & %s+%s-%s a -%s b+c=0 \\\\ & %s+%s-%s a -%s b+c=0.}$ \\\\ '
                        'Giải hệ phương trình ta được $\\heva{& a=%s \\\\ & b=%s \\\\ & c=%s.}$ \\\\'
                        'Suy ra đường tròn có tâm là $I(%s;%s)\\Rightarrow a=%s;b=%s$. Vậy $a+b=%s$.'

                        %(latex(x_a**2), latex(y_a**2), latex(2*x_a), latex(2*y_a), 
                            latex(x_b**2), latex(y_b**2), latex(2*x_b), latex(2*y_b), latex(x_c**2), 
                            latex(y_c**2), latex(2*x_c), latex(2*y_c), latex(a), latex(b), 
                            latex(c), latex(a), latex(b), latex(a), latex(b), latex(a+b)))


                #Đáp án
                dapan='  \\shortans[0]{$%s$}   \n'%(latex(a+b))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('-+','-').replace('+-', '-').replace('--', '+').replace('21\\vec', '21f\\vec').replace('51\\vec', '51f\\vec').replace('81\\vec', '81f\\vec').replace('1\\vec', '\\vec').replace('21f\\vec', '21\\vec').replace('51f\\vec', '51\\vec').replace('81f\\vec', '81\\vec')
            return content

