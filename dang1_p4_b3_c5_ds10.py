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


def bt_dang1_p4_b3_c5_ds10(self):
            # Khai báo biến
            #lisdang=['1','2','3','4','5']
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                n=randint(4,6)
                a=randint(2,4)
                b=randint(-5,-1)
                f=a*x+b
                A1=math.comb(4,0)
                A2=math.comb(4,1)
                A3=math.comb(4,2)
                A4=math.comb(4,3)
                A5=math.comb(4,4)


                # Nội dung câu hỏi
                noidungcauhoi = ('\\begin{enumEX}[a)]{1} \n'
                                '\\item Khai triển $\\left(%s\\right)^4$.'
                                '\\item Tìm hệ số của $x^2$ trong khai triển $\\left(%s\\right)^4$.'
                                '\\end{enumEX} \n'
                                %(latex(f),latex(f)
                                ))

                # Nội dung lời giải
                loigiai = (    '\\begin{enumEX}[a)]{1} \n'
                                '\\item Áp dụng công thức nhị thức Newton ta có \\\\ \n'
                                        '$\\left(%s\\right)^4=C_{4}^{0}\\cdot(%sx)^4\\cdot (%s)^0+C_{4}^{1}\\cdot(%sx)^3\\cdot (%s)^1+C_{4}^{2}\\cdot(%sx)^2\\cdot (%s)^2+C_{4}^{3}\\cdot(%sx)^1\\cdot (%s)^3+C_{4}^{4}\\cdot(%sx)^0\\cdot (%s)^4 $\\\\ \n'
                                        '$=%s\\cdot %sx^4\\cdot %s+%s\\cdot %sx^3\\cdot (%s)+%s\\cdot %sx^2\\cdot %s+%s\\cdot %sx^1\\cdot (%s)+%s\\cdot %sx^0\\cdot %s$\\\\ \n'
                                            '$=%sx^4+%sx^3+%sx^2+%sx+%s$'


                                '\\item  Từ khai triển ý $a\\text{)}$ ta có hệ số của $x^2$ trong khai triển $\\left(%s\\right)^4$ là $%s$ \n'

                                '\\end{enumEX} \n'

                        %(latex(f),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(A1),latex(a**4),latex(b**0),latex(A2),latex(a**3),latex(b**1),latex(A3),latex(a**2),latex(b**2),latex(A4),latex(a**1),latex(b**3),latex(A5),latex(a**0),latex(b**4),
                            latex(A1*a**4*b**0),latex(A2*a**3*b**1),latex(A3*a**2*b**2),latex(A4*a**1*b**3),latex(A5*b**4),
                            latex(f),latex(A3*a**2*b**2),
                            )
                        )

            if dang=='2':
                x=symbols('x')
                n=randint(4,6)
                a=randint(2,4)
                b=randint(-5,-1)
                f=a*x+b
                A1=math.comb(4,0)
                A2=math.comb(4,1)
                A3=math.comb(4,2)
                A4=math.comb(4,3)
                A5=math.comb(4,4)


                # Nội dung câu hỏi
                noidungcauhoi = ('\\begin{enumEX}[a)]{1} \n'
                                'a) Khai triển $\\left(%s\\right)^4$. '
                                'b) Tìm hệ số của $x^3$ trong khai triển $\\left(%s\\right)^4$.'
                                '\\end{enumEX} \n'
                                %(latex(f),latex(f)
                                ))

                # Nội dung lời giải
                loigiai = (    '\\begin{enumEX}[a)]{1} \n'
                                '\\item Áp dụng công thức nhị thức Newton ta có \\\\ \n'
                                        '$\\left(%s\\right)^4=C_{4}^{0}\\cdot(%sx)^4\\cdot (%s)^0+C_{4}^{1}\\cdot(%sx)^3\\cdot (%s)^1+C_{4}^{2}\\cdot(%sx)^2\\cdot (%s)^2+C_{4}^{3}\\cdot(%sx)^1\\cdot (%s)^3+C_{4}^{4}\\cdot(%sx)^0\\cdot (%s)^4 $\\\\ \n'
                                        '$=%s\\cdot %sx^4\\cdot %s+%s\\cdot %sx^3\\cdot (%s)+%s\\cdot %sx^2\\cdot %s+%s\\cdot %sx^1\\cdot (%s)+%s\\cdot %sx^0\\cdot %s$\\\\ \n'
                                            '$=%sx^4+%sx^3+%sx^2+%sx+%s$'


                                '\\item  Từ khai triển ý $a\\text{)}$ ta có hệ số của $x^3$ trong khai triển $\\left(%s\\right)^4$ là $%s$ \n'

                                '\\end{enumEX} \n'

                        %(latex(f),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(A1),latex(a**4),latex(b**0),latex(A2),latex(a**3),latex(b**1),latex(A3),latex(a**2),latex(b**2),latex(A4),latex(a**1),latex(b**3),latex(A5),latex(a**0),latex(b**4),
                            latex(A1*a**4*b**0),latex(A2*a**3*b**1),latex(A3*a**2*b**2),latex(A4*a**1*b**3),latex(A5*b**4),
                            latex(f),latex(A2*a**3*b**1),
                            )
                        )

            if dang=='3':
                x=symbols('x')
                n=randint(4,6)
                a=randint(2,4)
                b=randint(-5,-1)
                f=a*x+b
                A1=math.comb(5,0)
                A2=math.comb(5,1)
                A3=math.comb(5,2)
                A4=math.comb(5,3)
                A5=math.comb(5,4)
                A6=math.comb(5,5)


                # Nội dung câu hỏi
                noidungcauhoi = ('\\begin{enumEX}[a)]{1} \n'
                                'a) Khai triển $\\left(%s\\right)^5$. '
                                'b) Tìm hệ số của $x^4$ trong khai triển $\\left(%s\\right)^5$.'
                                '\\end{enumEX} \n'
                                %(latex(f),latex(f)
                                ))

                # Nội dung lời giải
                loigiai = (    '\\begin{enumEX}[a)]{1} \n'
                                '\\item Áp dụng công thức nhị thức Newton ta có \\\\ \n'
                                        '$\\left(%s\\right)^5=C_{5}^{0}\\cdot(%sx)^5\\cdot (%s)^0 +C_{5}^{1}\\cdot(%sx)^4\\cdot (%s)^1+C_{5}^{2}\\cdot(%sx)^3\\cdot (%s)^2+C_{5}^{3}\\cdot(%sx)^2\\cdot (%s)^3+C_{5}^{4}\\cdot(%sx)^1\\cdot (%s)^4+C_{5}^{5}\\cdot(%sx)^0\\cdot (%s)^5 $\\\\ \n'
                                        '$=%s\\cdot %sx^5\\cdot %s+%s\\cdot %sx^4\\cdot (%s)+%s\\cdot %sx^3\\cdot %s+%s\\cdot %sx^2\\cdot (%s)+%s\\cdot %sx^1\\cdot %s+%s\\cdot %sx^0\\cdot (%s)$\\\\ \n'
                                            '$=%sx^5+%sx^4+%sx^3+%sx^2+%sx+%s$'


                                '\\item  Từ khai triển ý $a\\text{)}$ ta có hệ số của $x^4$ trong khai triển $\\left(%s\\right)^4$ là $%s$ \n'

                                '\\end{enumEX} \n'

                        %(latex(f),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(A1),latex(a**5),latex(b**0),latex(A2),latex(a**4),latex(b**1),latex(A3),latex(a**3),latex(b**2),latex(A4),latex(a**2),latex(b**3),latex(A5),latex(a**1),latex(b**4),latex(A6),latex(a**0),latex(b**5),
                            latex(A1*a**5*b**0),latex(A2*a**4*b**1),latex(A3*a**3*b**2),latex(A4*a**2*b**3),latex(A5*a**1*b**4),latex(A6*a**0*b**5),
                            latex(f),latex(A2*a**4*b**1),
                            )
                        )

            if dang=='4':
                x=symbols('x')
                n=randint(4,6)
                a=randint(2,4)
                b=randint(-5,-1)
                f=a*x+b
                A1=math.comb(5,0)
                A2=math.comb(5,1)
                A3=math.comb(5,2)
                A4=math.comb(5,3)
                A5=math.comb(5,4)
                A6=math.comb(5,5)


                # Nội dung câu hỏi
                noidungcauhoi = ('\\begin{enumEX}[a)]{1} \n'
                                'a) Khai triển $\\left(%s\\right)^5$.'
                                'b) Tìm hệ số của $x^3$ trong khai triển $\\left(%s\\right)^5$.'
                                '\\end{enumEX} \n'
                                %(latex(f),latex(f)
                                ))

                # Nội dung lời giải
                loigiai = (    '\\begin{enumEX}[a)]{1} \n'
                                '\\item Áp dụng công thức nhị thức Newton ta có \\\\ \n'
                                        '$\\left(%s\\right)^5=C_{5}^{0}\\cdot(%sx)^5\\cdot (%s)^0 +C_{5}^{1}\\cdot(%sx)^4\\cdot (%s)^1+C_{5}^{2}\\cdot(%sx)^3\\cdot (%s)^2+C_{5}^{3}\\cdot(%sx)^2\\cdot (%s)^3+C_{5}^{4}\\cdot(%sx)^1\\cdot (%s)^4+C_{5}^{5}\\cdot(%sx)^0\\cdot (%s)^5 $\\\\ \n'
                                        '$=%s\\cdot %sx^5\\cdot %s+%s\\cdot %sx^4\\cdot (%s)+%s\\cdot %sx^3\\cdot %s+%s\\cdot %sx^2\\cdot (%s)+%s\\cdot %sx^1\\cdot %s+%s\\cdot %sx^0\\cdot (%s)$\\\\ \n'
                                            '$=%sx^5+%sx^4+%sx^3+%sx^2+%sx+%s$'


                                '\\item  Từ khai triển ý $a\\text{)}$ ta có hệ số của $x^3$ trong khai triển $\\left(%s\\right)^4$ là $%s$ \n'

                                '\\end{enumEX} \n'

                        %(latex(f),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(A1),latex(a**5),latex(b**0),latex(A2),latex(a**4),latex(b**1),latex(A3),latex(a**3),latex(b**2),latex(A4),latex(a**2),latex(b**3),latex(A5),latex(a**1),latex(b**4),latex(A6),latex(a**0),latex(b**5),
                            latex(A1*a**5*b**0),latex(A2*a**4*b**1),latex(A3*a**3*b**2),latex(A4*a**2*b**3),latex(A5*a**1*b**4),latex(A6*a**0*b**5),
                            latex(f),latex(A3*a**3*b**2),
                            )
                        )

            if dang=='5':
                x=symbols('x')
                n=randint(4,6)
                a=randint(2,4)
                b=randint(-5,-1)
                f=a*x+b
                A1=math.comb(5,0)
                A2=math.comb(5,1)
                A3=math.comb(5,2)
                A4=math.comb(5,3)
                A5=math.comb(5,4)
                A6=math.comb(5,5)


                # Nội dung câu hỏi
                noidungcauhoi = ('\\begin{enumEX}[a)]{1} \n'
                                'a) Khai triển $\\left(%s\\right)^5$. '
                                'b) Tìm hệ số của $x^2$ trong khai triển $\\left(%s\\right)^5$.'
                                '\\end{enumEX} \n'
                                %(latex(f),latex(f)
                                ))

                # Nội dung lời giải
                loigiai = (    '\\begin{enumEX}[a)]{1} \n'
                                '\\item Áp dụng công thức nhị thức Newton ta có \\\\ \n'
                                        '$\\left(%s\\right)^5=C_{5}^{0}\\cdot(%sx)^5\\cdot (%s)^0 +C_{5}^{1}\\cdot(%sx)^4\\cdot (%s)^1+C_{5}^{2}\\cdot(%sx)^3\\cdot (%s)^2+C_{5}^{3}\\cdot(%sx)^2\\cdot (%s)^3+C_{5}^{4}\\cdot(%sx)^1\\cdot (%s)^4+C_{5}^{5}\\cdot(%sx)^0\\cdot (%s)^5 $\\\\ \n'
                                        '$=%s\\cdot %sx^5\\cdot %s+%s\\cdot %sx^4\\cdot (%s)+%s\\cdot %sx^3\\cdot %s+%s\\cdot %sx^2\\cdot (%s)+%s\\cdot %sx^1\\cdot %s+%s\\cdot %sx^0\\cdot (%s)$\\\\ \n'
                                            '$=%sx^5+%sx^4+%sx^3+%sx^2+%sx+%s$'


                                '\\item  Từ khai triển ý $a\\text{)}$ ta có hệ số của $x^2$ trong khai triển $\\left(%s\\right)^4$ là $%s$ \n'

                                '\\end{enumEX} \n'

                        %(latex(f),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),
                            latex(A1),latex(a**5),latex(b**0),latex(A2),latex(a**4),latex(b**1),latex(A3),latex(a**3),latex(b**2),latex(A4),latex(a**2),latex(b**3),latex(A5),latex(a**1),latex(b**4),latex(A6),latex(a**0),latex(b**5),
                            latex(A1*a**5*b**0),latex(A2*a**4*b**1),latex(A3*a**3*b**2),latex(A4*a**2*b**3),latex(A5*a**1*b**4),latex(A6*a**0*b**5),
                            latex(f),latex(A4*a**2*b**3),
                            )
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

