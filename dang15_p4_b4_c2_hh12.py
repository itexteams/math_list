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


def bt_dang15_p4_b4_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                z=symbols('z')
                m=symbols('m')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=4
                e=randint(-9,9)

                while c==0 or a==0 or b==0 or e==0 or 2*a**2+2*b**2+2*c**2+2*a*b+2*b*c+2*c*a-e<=0:
                    x=symbols('x')
                    y=symbols('y')
                    z=symbols('z')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=4
                    e=randint(-9,9)
                delta=2*a**2+2*b**2+2*c**2+2*a*b+2*b*c+2*c*a-e
                hsb=a+b+c
                hsc=a**2+b**2+c**2-e
                x1=-hsb-sqrt(delta)
                x2=-hsb+sqrt(delta)

                mc1=(m-a)
                mc2=(m-b)
                mc3=(m-c)
                mcd=d*m**2+e
                a1=(x-a)**2
                b1=(y-b)**2
                c1=(z-c)**2
                a2=(x+a)**2
                b2=(y+b)**2
                c2=(z+c)**2
                r=abs(c)

                # Xác định khoảng giá trị
                start = x1
                end = x2

            # Lấy số nguyên gần nhất
                start_int = math.ceil(start)  # Lấy giá trị nguyên lớn hơn hoặc bằng -3.4
                end_int = math.floor(end)    # Lấy giá trị nguyên nhỏ hơn hoặc bằng 5.6

            # Tính số lượng số nguyên trong khoảng
                count = end_int - start_int + 1

                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, tìm tất cả các tham số $m$ để phương trình $$x^2+y^2+z^2+2(%s)x+2(%s)y+2(%s)z+%s=0$$ là phương trình mặt cầu.'
                                %(latex(mc1),latex(mc2),latex(mc3),latex(mcd)))

                loigiai=('Ta có $\\heva{&a=-m+%s\\\\&b=-m+%s\\\\&c=-m+%s\\\\&d=%s}$\\\\ \n'
                        'Phương trình trên là phương trình mặt cầu khi.\\\\ \n'
                        '$(-m+%s)^2+(-m+%s)^2+(-m+%s)^2-(%s)>0 \\Leftrightarrow -m^2 +%sm+%s>0\\\\ \n'
                        '\\Leftrightarrow %s<m<%s$.'
                        %(latex(a),latex(b),latex(c),latex(mcd),
                        latex(a),latex(b),latex(c),latex(mcd),latex(-hsb*2),latex(hsc),latex(x1),latex(x2),)
                        )




            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content  

