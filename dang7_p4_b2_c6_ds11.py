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


def bt_dang7_p4_b2_c6_ds11(self):
            # Khai báo biến
            # nam: số học sinh nam, nu: số học sinh nữ, chon: số học sinh được chọn
            nam = random.randint(12, 18)
            nu = random.randint(10, 15)
            tong = nam + nu
            chon = 3

            # Tính toán các giá trị tổ hợp
            # nO: không gian mẫu, nA: chọn 3 nam, nB: chọn 3 nữ
            nO = math.comb(tong, chon)
            nA = math.comb(nam, chon)
            nB = math.comb(nu, chon)

            # Tính xác suất
            prob = (nA + nB) / nO
            kq_num = round(prob, 3)
            kq = str("{:.3f}".format(kq_num)).replace('.', ',')

            # Các đáp án trắc nghiệm
            da = str(kq)
            # Tạo các đáp án sai không trùng với đáp án đúng
            s = set()
            while len(s) < 3:
                sai_num = round(prob + random.choice([-0.05, 0.05, -0.08, 0.08, -0.1, 0.1]), 3)
                sai_str = str("{:.3f}".format(sai_num)).replace('.', ',')
                if sai_str != da and sai_num > 0:
                    s.add(sai_str)

            list_sai = list(s)
            das1 = list_sai[0]
            das2 = list_sai[1]
            das3 = list_sai[2]

            # Câu hỏi
            noidungcauhoi = (
                "Một lớp học có " + str(tong) + " học sinh trong đó có " + str(nam) + " bạn nam và " + str(nu) + " bạn nữ. "
                "Cô giáo chủ nhiệm chọn ngẫu nhiên ra " + str(chon) + " bạn vào đội cờ đỏ. "
                "Tính xác suất để cả " + str(chon) + " bạn đó đều là nam hoặc nữ."
            )

            # Các đáp án
            da_d = "\\True " + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = (
                "Chọn " + str(chon) + " bạn trong " + str(tong) + " bạn có: $C_{" + str(tong) + "}^{" + str(chon) + "}$ cách chọn "
                "$\\Rightarrow n(\\Omega) = C_{" + str(tong) + "}^{" + str(chon) + "} = " + str(nO) + "$. \\\\ "
                "Gọi $A$ là biến cố \"Chọn " + str(chon) + " bạn nam\" $\\Rightarrow n(A) = C_{" + str(nam) + "}^{" + str(chon) + "} = " + str(nA) + " \\Rightarrow P(A) = \\frac{C_{" + str(nam) + "}^{" + str(chon) + "}}{C_{" + str(tong) + "}^{" + str(chon) + "}}$. \\\\ "
                "Gọi $B$ là biến cố \"Chọn " + str(chon) + " bạn nữ\" $\\Rightarrow n(B) = C_{" + str(nu) + "}^{" + str(chon) + "} = " + str(nB) + " \\Rightarrow P(B) = \\frac{C_{" + str(nu) + "}^{" + str(chon) + "}}{C_{" + str(tong) + "}^{" + str(chon) + "}}$. \\\\ "
                "Gọi $C$ là biến cố \"Chọn " + str(chon) + " bạn đều là nam hoặc nữ\" $\\Rightarrow C = A \\cup B$. \\\\ "
                "Do $A$ và $B$ xung khắc nên: \\\\ "
                "$P(C) = P(A) + P(B) = \\frac{" + str(nA) + "}{" + str(nO) + "} + \\frac{" + str(nB) + "}{" + str(nO) + "} \\approx " + str(kq) + "$."
            )

            # Xuất câu trắc nghiệm (không dùng raw string r)
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

