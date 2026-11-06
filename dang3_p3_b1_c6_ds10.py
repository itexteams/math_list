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


def bt_dang3_p3_b1_c6_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                a=randint(5,20)
                b=randint(5,20)
                c=randint(5,20)

                d=randint(5,20)
                e=randint(5,20)
                f=randint(5,20)

                kq1=Rational(a*d+b*e+c*f,(a+b+c)*(d+e+f))

                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Câu hỏi
                noidungcauhoi = ('Hộp $A$ có $%s$ viên bi trắng, $%s$ viên bi đỏ và $%s$ viên bi xanhzzz Hộp $B$ có $%s$ viên bi trắng, $%s$ viên bi đỏ và $%s$ viên bi xanhzzz'
                                ' Lấy ngẫu nhiên mỗi hộp một viên bi, xác suất để hai viên bi được lấy ra có cùng màu là bao nhiêu (kết quả làm tròn đến hàng phần trăm)?'
                                %(latex(a),latex(b),latex(c),latex(d),latex(e),latex(f),)
                                )

                # Nội dung lời giải
                loigiai = ('Hộp $A$ có số bi là $%s+%s+%s=%s$, hộp $B$ có số bi là $%s+%s+%s=%s$zzz Lấy ngẫu nhiên mỗi hộp một viên bi nên số phần tử của không gian mẫu là $n(\\Omega)=%s\\cdot %s=%s$zzz\\\\ \n'
                        'Gọi $C$ là biến cố "Lấy được hai viên bi cùng màu"zzz\\\\ \n'
                        'Số cách chọn được hai viên bi màu trắng từ mỗi hộp là $%s\\cdot %s=%s$zzz\\\\ \n'
                        'Số cách chọn được hai viên bi màu đỏ từ mỗi hộp là $%s\\cdot %s=%s$zzz\\\\ \n'
                        'Số cách chọn được hai viên bi màu xanh từ mỗi hộp là $%s\\cdot %s=%s$zzz\\\\ \n'
                        'Số cách chọn được hai viên bi cùng màu là $n(C)=%s+ %s +%s=%s$zzz\\\\ \n'
                        'Vậy xác suất cần tìm là $P(C)=\\dfrac{n(C)}{n(\\Omega)}=%s\\approx %s$zzz'

                        %(latex(a),latex(b),latex(c),latex(a+b+c),latex(d),latex(e),latex(f),latex(d+e+f),latex(a+b+c),latex(d+e+f),latex((a+b+c)*(d+e+f)),
                            latex(a),latex(d),latex(a*d),
                            latex(b),latex(e),latex(b*e),
                            latex(c),latex(f),latex(c*f),
                            latex(a*d),latex(b*e),latex(c*f),latex(a*d+b*e+c*f),
                            latex(kq1),latex(kq),
            )
                        )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zzz', '.')
            return content  

