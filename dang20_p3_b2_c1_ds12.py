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


def bt_dang20_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                k=randint(3,9)
                a=5*k #phí
                b=80
                c=10
                d=25
                x=symbols('x')                    
                t1=Rational(80,1000)*(25*(x-1))
                t2=Rational(80,1000)*(25*(x-2))
                t3=Rational(80,1000)*25

                y=(x**2-x+a)/x

                # Tạo danh sách các x và y tương ứng
                x_list = [1,2,3,4,5,6,7,8,9,10]
                y1=Rational(1**2-1+a,1)
                y2=Rational(2**2-2+a,2)
                y3=Rational(3**2-3+a,3)
                y4=Rational(4**2-4+a,4)
                y5=Rational(5**2-5+a,5)
                y6=Rational(6**2-6+a,6) 
                y7=Rational(7**2-7+a,7)
                y8=Rational(8**2-8+a,8)
                y9=Rational(9**2-9+a,9)
                y10=Rational(10**2-10+a,10)

                y_list = [Rational(x**2 - x + a, x) for x in x_list]

                # Tìm giá trị nhỏ nhất trong y_list
                gtnn = min(y_list)

                # Tìm chỉ số của giá trị nhỏ nhất
                index_min = y_list.index(gtnn)

                # Lấy ra x tương ứng
                x_ket_qua = x_list[index_min]

                h1=1 
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một đại lý nhập khẩu trái cây tươi để phân phối cho các cửa hàng. Mỗi lần nhập khẩu trái cây, khoán chi phí vận chuyển (không đổi) là $%s$ triệu đồng. Chi phí bảo quản mỗi tạ trái cây dự trữ trong kho là $%s$ nghìn đồng/ngày. Thời gian bảo quản trái cây trong kho tối đa $%s$ ngày. Biết rằng, kể từ ngày đầu tiên nhập hàng, đại lý sẽ phân phối tới các cửa hàng $%s$ tạ trái cây mỗi ngày. Mỗi lần nhập hàng, đại lý phải nhập đủ trái cây cho bao nhiêu ngày phân phối để chi phí trung bình cho mỗi ngày thấp nhất (bao gồm chi phí vận chuyển và chi phí bảo quản trong kho)? '''
                                %(latex(a),latex(b),latex(c),latex(d)
                                ))

                # Nội dung lời giải
                loigiai = ('''Giả sử mỗi lần nhập hàng, đại lý phải nhập đủ trái cây cho $x$ ngày, $x \\in \\mathbb{N}^*, x \\le %s$.\\\\
                        Khối lượng trái cây là $%s x$ (tạ). \\\\ 
                            Tiền phí vận chuyển là $%s$ triệu. \\\\
                            Sau một ngày, tiền bảo quản là $%s \\left[%s (x-1)\\right]=%s(x-1)$. \\\\
                                Sau hai ngày, tiền bảo quản là $%s \\left[%s (x-2)\\right]=%s(x-2)$. \\\\ 
                                Sau $x-1$ ngày, tiền bảo quản là $%s$ triệu. \\\\
                                Sau $x$ ngày hết hàng. \\\\
                                Tổng số tiền bảo quản và vận chuyển là \\\\
                                $%s \\left[ (x-1)+(x-2)+ \\dots +1 \\right]+%s=%s \\cdot \\frac{x(x-1)}{2}+%s=x^2-x+%s$. \\\\
                                Chi phí trung bình cho mỗi ngày là $\\frac{x^2-x+%s}{x}$. \\\\
                                Đặt $f(x)=\\frac{x^2-x+%s}{x}$, ta có \\\\
                                $f(1)=%s; f(2)=%s, f(3)=%s; f(4)=%s; f(5)=%s; $ \\\\
                                $f(6)=%s; f(7)=%s; f(8)=%s; f(9)=%s; f(10)=%s$. \\\\
                                Chi phí trung bình nhỏ nhất là $%s$. \\\\
                                    Vậy đại lý phải nhập đủ trái cây cho $%s$ ngày phân phối để chi phí trung bình cho mỗi ngày thấp nhất.'''
                        %(latex(c),
                            latex(d),
                            latex(a),
                            latex(Rational(b,1000)),latex(d),latex(t3),
                            latex(Rational(b,1000)),latex(d),latex(t3),
                            latex(t3),
                            latex(t3),latex(a),latex(t3),latex(a),latex(a),
                            latex(a),latex(a),
                            latex(y1),latex(y2),latex(y3),latex(y4),latex(y5),latex(y6),latex(y7),latex(y8),latex(y9),latex(y10),
                            latex(gtnn),
                            latex(x_ket_qua )
                        ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(x_ket_qua ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

