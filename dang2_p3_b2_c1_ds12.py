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


def bt_dang2_p3_b2_c1_ds12(self):
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(1,30)
                f=(a-x)/2*sqrt(2*a*x-a**2)
                daoham=(2*a**2-3*a*x)/(2*sqrt(2*x-a**2))
                x0=Rational(2*a,3)
                f0=1/2*(a-0)*sqrt(2*a*0-a**2)
                fx=Rational(a-x0,2)*sqrt(2*a*x0-a**2)
                fa=1/2*(a-a)*sqrt(2*a*a-a**2)

                number = Decimal(float(fx))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Trong số các tam giác vuông có tổng một cạnh góc vuông và cạnh huyền bằng $%s$, tam giác có diện tích lớn nhất bằng bao nhiêu? (Làm tròn kết quả đến hàng phần chục)$zz$ \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('Xét tam giác $ABC$ vuông tại $A$ và thỏa mãn yêu cầu đề bài$zz$ \\\\ \n'
                        'Giả sử $AB+BC=%s \\Rightarrow AB=%s-BC$$zz$ \\\\ \n'
                        'Đặt $BC=x$ với $0<x<%s$, suy ra \\\\ \n'
                        '\\hspace*{1cm} $AB=%s-x$ và $AC=\\sqrt{x^2-(%s-x)^2}=\\sqrt{2\\cdot %s x-%s^2}$$zz$\\\\ \n'
                        '\\hspace*{1cm} Diện tích tam giác $ABC$ là $S=\\dfrac{1}{2}AB \\cdot AC = \\dfrac{1}{2} (%s-x)\\sqrt{2 \\cdot %s x-%s^2}$$zz$ \\\\ \n'
                        'Xét hàm số $f(x)=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=%s$$zz$\\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow x=%s$$zz$\\\\ \n'
                        '\\hspace*{1cm} Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm}\\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5] \n'
                        '{$x$/1,$f\'(x)$/0$zz$7,$f(x)$/2$zz$1} \n'
                        '{$0$,$%s$,$%s$} \n'
                        '\\tkzTabLine{,+,0,-,} \n'
                        '\\tkzTabVar{-/,+/$%s$,-/}  \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta thấy giá trị lớn nhất của hàm số $f(x)$ bằng $%s$$zz$ \\\\ \n'
                        'Vậy diện tích lớn nhất của tam giác $ABC$ là $%s \\approx %s$'

                        %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),
                            latex(f),
                            latex(daoham),
                            latex(x0),
                            latex(x0),latex(a),
                            latex(fx),latex(fx),
                            latex(fx),latex(kq)
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content    

