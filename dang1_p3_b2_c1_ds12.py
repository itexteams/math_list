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


def bt_dang1_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(50,80)
                x1=Rational(a,4)
                b=Rational(a,2)
                f=a*x-2*x**2
                fa=0 
                f1=a*x1-2*x1**2
                fb=a*b-2*b**2
                number = Decimal(float(f1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Người ta muốn rào quanh một khu đất hình chữ nhật với một số vật liệu cho trước là $%s$ m thẳng hàng rào$zz$ Tại khu đất người ta tận dụng một bờ giậu có sẵn để làm một cạnh của hàng rào$zz$ Có thể rào được khu đất với diện tích lớn nhất bằng bao nhiêu? (Làm tròn kết quả đến hàng đơn vị)$zz$ \n'
                                %(latex(a))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $x$ là chiều dài cạnh song song với bờ giậu $(x>0)$$zz$ \\\\ \n'
                        '\\hspace*{0$zz$6cm} $y$ là chiều rộng cạnh vuông góc với bờ giậu $(y>0)$$zz$ \\\\ \n'
                        'Theo bài toán ta có \\\\ \n'
                        '\\hspace*{0$zz$6cm} $x+2y=%s \\Leftrightarrow x=%s-2y$ suy ra $0<y<%s$$zz$\\\\ \n'
                        'Khi đó diện tích khu đất là $S=xy=y(%s-2y)=%sy-2y^2$$zz$\\\\ \n'
                        'Đặt $f(y)=%sy-2y^2$ với $0<y<%s$, ta có \\\\ \n'
                        '\\hspace*{0$zz$6cm} $f\'(y)=%s-4y$$zz$\\\\ \n'
                        '\\hspace*{0$zz$6cm} $f\'(y)=0 \\Leftrightarrow y=%s$$zz$\\\\ \n'
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{0$zz$6cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5]  \n'
                        '{$y$/1,$f\'(y)$/0$zz$7,$f(y)$/2$zz$1} \n'
                        '{$0$,$%s$,$%s$} \n'
                        '\\tkzTabLine{,+, 0 ,-,} \n'
                        '\\tkzTabVar{-/$%s$,+/$%s$,-/$%s$} \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta thấy giá trị lớn nhất của $f(y)$ là $%s$$zz$\\\\ \n'
                        'Vậy có thể rào được khu đất có diện tích lớn nhất bằng $%s \\approx %s$ m$^2$$zz$'
                        %(latex(a),latex(a),latex(Rational(a,2)),
                            latex(a),latex(a),
                            latex(a),latex(Rational(a,2)),
                            latex(a),latex(Rational(a,4)),
                            latex(Rational(a,4)),latex(Rational(a,2)),
                            latex(fa),latex(f1),latex(fb),
                            latex(f1),
                            latex(f1),latex(kq),
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace(',0', '')
            return content

