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


def bt_dang21_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                k=randint(1,3)
                gia=300*k
                so_luong=100*k
                gia_giam=10*k
                ban_them=10*k

                f=(gia-gia_giam*x)*(so_luong+ban_them*x)
                y=expand(f)

                dh=diff(f,x)
                pt=Eq(dh,0)
                nghiem=solve(pt,x)
                x0=nghiem[0]

                f0=(gia-gia_giam*0)*(so_luong+ban_them*0)
                fx0=(gia-gia_giam*x0)*(so_luong+ban_them*x0)
                f30=(gia-gia_giam*30)*(so_luong+ban_them*30)

                #h1=1
                #number = Decimal(float(h1))  # Số cần làm tròn
                #kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                #kq1=str(kq).replace('.', ',')
                kq=gia-gia_giam*x0
                # Nội dung câu hỏi
                noidungcauhoi = ('''Một nhà hàng bán buffet hải sản. Nếu nhà hàng bán với giá $%s$ nghìn đồng một suất thì mỗi ngày nhà hàng bán được $%s$ suất. Nhà hàng dự định có đợt giảm giá bán để kích cầu trong dịp cuối năm. Theo khảo sát từ thị trường thì mỗi lần giảm giá $%s$ nghìn đồng một suất thì nhà hàng bán thêm được $%s$ suất. Tìm giá (đơn vị: nghìn đồng) một suất nhà hàng cần bán để doanh thu trong một ngày là lớn nhất.'''
                                %(latex(gia),latex(so_luong),latex(gia_giam),latex(ban_them)
                                ))

                # Nội dung lời giải
                loigiai = ('''Gọi số tiền giảm giá một suất là $%s x$ (nghìn đồng), với $0 \\le x \\le 30$. \\\\
                        Khi đó, số suất bán thêm được là $%s x$ (suất). \\\\
                            Sau khi giảm giá ta có \\\\
                                \\hspace*{1cm} + Giá bán mới là $(%s-%s x)$ ngàn đồng/1 suất. \\\\
                                \\hspace*{1cm} + Số suất bán được là $(%s+%s x)$ suất. \\\\
                                \\hspace*{1cm} + Doanh thu (đơn vị: nghìn đồng) trong một ngày của nhà hàng là \\\\
                                \\hspace*{1cm} $f(x)=%s=%s$ với $0 \\le x \\le 30$. \\\\
                                \\hspace*{1cm} Ta có \\\\
                                    \\hspace*{2cm} $f'(x)=%s$. \\\\
                                        \\hspace*{2cm}  $f'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\
                                        \\hspace*{1cm}  Bảng biến thiên \\\\
                                \\hspace*{1cm} \\begin{tikzpicture}
                            \\tkzTabInit[espcl=2.5,lgt=1.5]
                            {$x$/0.7,$f'(x)$/0.7,$f(x)$/2.1}
                            {$0$,$%s$,$30$}
                            \\tkzTabLine{,+,0,-}
                            \\tkzTabVar{-/$%s$,+/$%s$,-/$%s$}
                            \\end{tikzpicture} \\\\
                                Dựa vào bảng biến thiên, ta thấy cần bán với giá mới là: $%s-%s \\cdot %s=%s$ (ngàn đồng/1 suất) thì doanh thu trong một ngày là lớn nhất.'''
                        %(latex(gia_giam),
                            latex(ban_them),
                            latex(gia),latex(gia_giam),
                            latex(so_luong),latex(ban_them),
                            latex(f),latex(y),
                            latex(dh),
                            latex(dh),latex(x0),
                            latex(x0),
                            latex(f0),latex(fx0),latex(f30),
                            latex(gia),latex(gia_giam),latex(x0),latex(kq)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\left[', '').replace('\\right]', '')
            return content

