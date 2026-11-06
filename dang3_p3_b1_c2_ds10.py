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


def bt_dang3_p3_b1_c2_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                def format_number_with_space(number):
                    """
                    Định dạng số nguyên với dấu cách phân tách hàng nghìn.

                    Args:
                        number (int): Số nguyên cần định dạng.

                    Returns:
                        str: Chuỗi số đã định dạng.
                    """
                    return "{:,}".format(number).replace(",", " ")
                # Khai báo biến
                x,y = symbols('x,y')
                b=randint(3,12)
                m=randint(4,10)
                n=randint(12,25)
                t2=m*1000
                t1=n*1000
                p1=randint(200,400)
                p=p1*1000
                v=(p-b*t2)/t1
                kq=(p-b*t2)//t1
                f=t1*x+t2*y
                while v>20 or v<=3:
                    x,y = symbols('x,y')
                    b=randint(3,12)
                    m=randint(4,10)
                    n=randint(12,25)
                    t2=m*1000
                    t1=n*1000
                    p1=randint(200,400)
                    p=p1*1000
                    v=(p-b*t2)/t1
                    kq=(p-b*t2)//t1
                    f=t1*x+t2*y



                # Nội dung câu hỏi
                noidungcauhoi = ('Một học sinh đem $%s$ đồng đi nhà sách để mua một số quyển vở và bút$zz$ Biết rằng giá một quyển vở là $%s$ đồng và giá của '
                                 'một cây bút là $%s$ đồng$zz$ Học sinh đó có thể mua được tối đa bao nhiêu quyển vở nếu đã mua $%s$ cây bút$zz$'
                             %(latex(format_number_with_space(p)),latex(format_number_with_space(t1)),latex(format_number_with_space(t2)),latex(b)
                               )
                              )
                # Nội dung lời giải
                loigiai = ('Gọi $x,y$ lần lượt là số quyển vở và cây bút mà học sinh có thể mua $(x,y \\in \\mathbb{N})$$zz$\\\\ \n'
                           'Bất phương trình biểu diễn số quyển vở và bút có thể mua phụ thuộc vào số tiền mang theo là\\\\ \n'
                           '\\hspace*{1cm}$ %s\\leq %s$\\\\ \n'
                           'Vì bạn học sinh đó đã mua $%s$ cây bút nên ta có\\\\ \n'
                           '\\hspace*{1cm} $%s+%s\\cdot %s \\leq %s \\Leftrightarrow x \\leq %s$$zz$\\\\ \n'
                           'Vì $x \\in \\mathbb{N}$ nên số quyển vở tối đa có thể mua là $%s$$zz$'

                         %(latex(f),latex(p),latex(b),latex(t1*x),latex(t2),latex(b),
                             latex(p),latex(v),latex(kq)

                           ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            if dang=='2':
                def format_number_with_space(number):
                    """Định dạng số nguyên với dấu cách phân tách hàng nghìn.
                    Args:
                        number (int): Số nguyên cần định dạng.
                    Returns:
                        str: Chuỗi số đã định dạng."""
                    return "{:,}".format(number).replace(",", " ")
                # Khai báo biến
                x,y = symbols('x,y')
                b=randint(10,20)
                m=randint(4,10)
                n=randint(12,25)
                t2=m*1000
                t1=n*1000
                p1=randint(200,400)
                p=p1*1000
                v=(p-b*t1)/t2
                kq=(p-b*t1)//t2
                f=t1*x+t2*y
                while v>20 or v<=3:
                    x,y = symbols('x,y')
                    b=randint(10,20)
                    m=randint(4,10)
                    n=randint(12,25)
                    t2=m*1000
                    t1=n*1000
                    p1=randint(200,400)
                    p=p1*1000
                    v=(p-b*t1)/t2
                    kq=(p-b*t1)//t2
                    f=t1*x+t2*y



                # Nội dung câu hỏi
                noidungcauhoi = ('Một học sinh đem $%s$ đồng đi nhà sách để mua một số quyển vở và bút$zz$ Biết rằng giá một quyển vở là $%s$ đồng và giá của '
                                 'một cây bút là $%s$ đồng$zz$ Học sinh đó có thể mua được tối đa bao nhiêu cây bút nếu bạn đã mua $%s$ quyển vở$zz$'
                             %(latex(format_number_with_space(p)),latex(format_number_with_space(t1)),latex(format_number_with_space(t2)),latex(b)
                               )
                              )
                # Nội dung lời giải
                loigiai = ('Gọi $x,y$ lần lượt là số quyển vở và cây bút mà học sinh có thể mua $(x,y \\in \\mathbb{N})$$zz$\\\\ \n'
                           'Bất phương trình biểu diễn số quyển vở và bút có thể mua phụ thuộc vào số tiền mang theo là\\\\ \n'
                           '\\hspace*{1cm}$ %s\\leq %s$\\\\ \n'
                           'Vì bạn học sinh đó đã mua $%s$ quyển vở nên ta có\\\\ \n'
                           '\\hspace*{1cm} $%s\\cdot %s + %s \\leq %s \\Leftrightarrow y \\leq %s$$zz$\\\\ \n'
                           'Vì $y \\in \\mathbb{N}$ nên số cây bút tối đa có thể mua là $%s$$zz$'

                         %(latex(f),latex(p),latex(b),latex(t1),latex(b),latex(t2*y),
                             latex(p),latex(v),latex(kq)

                           ))

                #Đáp án
                dapan='\\shortans[0]{$%s$} \n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content

