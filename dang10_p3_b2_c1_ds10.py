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


def bt_dang10_p3_b2_c1_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên
                n_X = randint(40, 50)
                n_A = randint(15, 25)
                n_B = randint(20, 30)
                n_not_A_not_B = randint(5, 15)

                # Tính toán để đảm bảo kết quả hợp lý
                n_A_union_B = n_X - n_not_A_not_B
                n_A_intersect_B = n_A + n_B - n_A_union_B

                # Đảm bảo kết quả là số nguyên dương
                if n_A_intersect_B < 0:
                    n_A_intersect_B = randint(1, 5)
                    n_A = n_A_union_B - n_B + n_A_intersect_B

                # Kết quả
                kq = n_A_intersect_B



                # Câu hỏi
                noidungcauhoi = ('''Lớp 10C có $%s$ học sinh, trong đó có $%s$ học sinh tham gia cuộc thi vẽ đồ họa trên máy tính, $%s$ học sinh tham gia cuộc thi tin học văn phòng cấp trường và $%s$ học sinh không tham gia cả hai cuộc thi này. Số học sinh của lớp 10C tham gia đồng thời hai cuộc thi là bao nhiêu?'''
                                 %(latex(n_X), latex(n_A), latex(n_B), latex(n_not_A_not_B)))



                # Nội dung lời giải
                loigiai=('''Gọi X là tập hợp các học sinh của lớp 10C. A là tập hợp các học sinh tham gia cuộc thi vẽ đồ họa trên máy tính, B là tập hợp các học sinh tham gia cuộc thi tin học văn phòng cấp trường. \\\\
                            Ta có: $|A|=%s$, $|B|=%s$, $|X|=%s$. Số học sinh không tham gia cuộc thi nào là $%s$.\\\\
                            Số học sinh tham gia ít nhất một trong hai cuộc thi là $|A \\cup B| = |X| - %s = %s - %s = %s$ (học sinh).\\\\
                            Áp dụng công thức: $|A \\cup B| = |A| + |B| - |A \\cap B|$.\\\\
                            Suy ra số học sinh tham gia cả hai cuộc thi là: $|A \\cap B| = |A| + |B| - |A \\cup B| = %s + %s - %s = %s$ (học sinh).\\\\
                            Vậy có $%s$ học sinh của lớp 10C tham gia đồng thời hai cuộc thi.'''
                          %(latex(n_A), latex(n_B), latex(n_X), latex(n_not_A_not_B), 
                            latex(n_not_A_not_B), latex(n_X), latex(n_not_A_not_B), latex(n_A_union_B),
                            latex(n_A), latex(n_B), latex(n_A_union_B), latex(kq),
                            latex(kq)
                          ))

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

