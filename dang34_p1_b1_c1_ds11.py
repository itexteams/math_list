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


def bt_dang34_p1_b1_c1_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tự động thay số
                duong_kinh_cm = random.randint(25, 35) + random.choice([0, 0.2, 0.4, 0.6, 0.8])
                so_vong = random.randint(8, 15)
                thoi_gian_giay = random.randint(3, 7)
                quang_duong_can_di = random.randint(400, 600)

                # Tính toán
                # Chuyển đổi đường kính từ cm sang m để tính toán chính xác
                duong_kinh_m = duong_kinh_cm / 100
                ban_kinh_m = duong_kinh_m / 2

                # Tính quãng đường đi được trong 1 giây (đơn vị: m)
                # Sử dụng float để tránh lỗi TypeError với pi
                quang_duong_1s = (so_vong / thoi_gian_giay) * 2 * math.pi * ban_kinh_m

                # Thời gian cần để đi hết quãng đường (đơn vị: giây)
                thoi_gian_can_di_giay = quang_duong_can_di / quang_duong_1s

                # Chuyển thời gian sang phút và làm tròn đến hàng đơn vị
                kq_phut = thoi_gian_can_di_giay / 60
                kq_phut_lam_tron = int(round(kq_phut))

                # Các đáp án trắc nghiệm
                du = ['$%s$ phút'%(latex(kq_phut_lam_tron)),]
                da= random.choice(du)

                s = ['$%s$ phút'%(latex(kq_phut_lam_tron + 1)),
                    '$%s$ phút'%(latex(kq_phut_lam_tron + 2)),
                    '$%s$ phút'%(latex(kq_phut_lam_tron - 1)),
                    '$%s$ phút'%(latex(kq_phut_lam_tron - 2)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Bánh xe của bé An có đường kính $%s$cm và quay được $%s$ vòng trong vòng $%s$ giâyzz Bé An đi được quãng đường $%s$ mét sau bao nhiêu phút (làm tròn đến hàng đơn vị)?'''
                                  %(latex(duong_kinh_cm),latex(so_vong),latex(thoi_gian_giay),latex(quang_duong_can_di)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Bán kính bánh xe là $\\frac{%s}{2}=%s$ cm $=%s$ mzz \\\\
                            Mỗi giây bé An đi được quãng đường là $\\frac{%s}{%s} \\cdot 2\\pi \\cdot %s \\approx %s$ mzz \\\\
                            Thời gian để đi quãng đường $%s$m là \\\\
                            $\\frac{%s}{%s} \\approx %s$ giây $\\approx %s$ phútzz'''
                            %(latex(duong_kinh_cm), latex(duong_kinh_cm/2), latex(ban_kinh_m),
                            latex(so_vong), latex(thoi_gian_giay), latex(ban_kinh_m), latex(round(quang_duong_1s, 2)),
                            latex(quang_duong_can_di), latex(quang_duong_can_di), latex(round(quang_duong_1s, 2)), 
                            latex(round(thoi_gian_can_di_giay, 1)), latex(kq_phut_lam_tron)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('zz','.')
            return content

