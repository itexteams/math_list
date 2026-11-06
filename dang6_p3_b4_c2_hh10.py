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


def bt_dang6_p3_b4_c2_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)                   

                while 2*x2-2*x1==0 or x1==x2 or x1==0 or x2==0 or y1==0 or y2==0 or (x2**2+y2**2-x1**2-y1**2)%(2*x2-2*x1)!=0:
                    x=symbols('x')
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                kq=nsimplify((x2**2+y2**2-x1**2-y1**2)/(2*x2-2*x1))
                lis1=['A','B','C','D']
                lis2=['E','F','G','H']
                lis3=['I','M','N','P']
                m=random.choice(lis1)
                n=random.choice(lis2)
                p=random.choice(lis3)


                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $%s(%s;%s)$ và %s(%s;%s), gọi $%s$ là điểm thuộc $Ox$ sao cho $%s%s=%s%s$. Hỏi tổng hoành độ và tung độ của điểm $%s$ bằng bao nhiêu? \\\\ \n'
                                %(m,latex(x1),latex(y1),n,latex(x2),latex(y2),p,m,p,n,p,p)
                                )

                # Nội dung lời giải
                loigiai = ('Vì điểm $%s$ thuộc trục $Ox$ nên tọa độ của $%s$ là $%s(x;0)$.\\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '&&%s%s=%s%s\\\\ \n'
                        '&\\Leftrightarrow& \\abs{\\vec{%s%s}}=\\abs{\\vec{%s%s}}\\\\ \n'
                        '&\\Leftrightarrow& \\sqrt{(x-%s)^2+(0-%s)^2}=\\sqrt{(x-%s)^2+(0-%s)^2}\\\\ \n'
                        '&\\Leftrightarrow& (x-%s)^2+(0-%s)^2=(x-%s)^2+(0-%s)^2\\\\ \n'
                        '&\\Leftrightarrow& x^2-%sx+%s+%s=x^2-%sx+%s+%s\\\\ \n'
                        '&\\Leftrightarrow& %sx=%s\\\\ \n'
                        '&\\Leftrightarrow&x=%s. \n'
                        '\\end{eqnarray*} \n'
                        'Suy ra $P(%s;0)$. Vậy tổng hoành độ và tung độ của điểm $P$ là $%s$. '
                        %(p,p,p,m,p,n,p,
                            m,p,n,p,
                            latex(x1),latex(y1),latex(x2),latex(y2),
                            latex(x1),latex(y1),latex(x2),latex(y2),
                            latex(2*x1),latex(x1**2),latex(y1**2),
                            latex(2*x2),latex(x2**2),latex(y2**2),
                            latex(2*(x2-x1)),latex(x2**2+y2**2-x1**2-y1**2),latex(kq),latex(kq),latex(kq))
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='2':
                x1=randint(-10,10)
                y1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)


                while 2*y2-2*y1==0 or  x1==x2 or x1==0 or x2==0 or y1==0 or y2==0 or (x2**2+y2**2-x1**2-y1**2)%(2*y2-2*y1)!=0:
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                kq=nsimplify((x2**2+y2**2-x1**2-y1**2)/(2*y2-2*y1))
                lis1=['A','B','C','D']
                lis2=['E','F','G','H']
                lis3=['I','M','N','P']
                m=random.choice(lis1)
                n=random.choice(lis2)
                p=random.choice(lis3)


                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $%s(%s;%s)$ và %s(%s;%s), gọi $%s$ là điểm thuộc $Oy$ sao cho $%s%s=%s%s$. Hỏi tổng hoành độ và tung độ của điểm $%s$ bằng bao nhiêu? \\\\ \n'
                                %(m,latex(x1),latex(y1),n,latex(x2),latex(y2),p,m,p,n,p,p)
                                )

                # Nội dung lời giải
                loigiai = ('Vì điểm $%s$ thuộc trục $Oy$ nên tọa độ của $%s$ là $%s(0;y)$.\\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '&&%s%s=%s%s\\\\ \n'
                        '&\\Leftrightarrow& \\abs{\\vec{%s%s}}=\\abs{\\vec{%s%s}}\\\\ \n'
                        '&\\Leftrightarrow& \\sqrt{(0-%s)^2+(y-%s)^2}=\\sqrt{(0-%s)^2+(y-%s)^2}\\\\ \n'
                        '&\\Leftrightarrow& (0-%s)^2+(y-%s)^2=(0-%s)^2+(y-%s)^2\\\\ \n'
                        '&\\Leftrightarrow& %s+y^2-%sy+%s=%s+y^2-%sy+%s\\\\ \n'
                        '&\\Leftrightarrow& %sy=%s\\\\ \n'
                        '&\\Leftrightarrow&y=%s. \n'
                        '\\end{eqnarray*} \n'
                        'Suy ra $P(0;%s)$. Vậy tổng hoành độ và tung độ của điểm $P$ là $%s$. '
                        %(p,p,p,m,p,n,p,
                            m,p,n,p,
                            latex(x1),latex(y1),latex(x2),latex(y2),
                            latex(x1),latex(y1),latex(x2),latex(y2),
                            latex(x1**2),latex(2*y1),latex(y1**2),
                            latex(x2**2),latex(2*y2),latex(y2**2),
                            latex(2*(y2-y1)),latex(x2**2+y2**2-x1**2-y1**2),latex(kq),latex(kq),latex(kq))
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-')
            return content   

