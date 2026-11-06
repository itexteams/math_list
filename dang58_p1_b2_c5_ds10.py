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


def bt_dang58_p1_b2_c5_ds10(self):
            # Khai báo biến
            # p_m: Số giáo viên Vật lý nam
            m_f = random.randint(3, 5)
            m_m = random.randint(4, 6)
            p_m = random.randint(3, 5)
            m_total = m_f + m_m

            # Tính toán các giá trị tổ hợp cho lời giải
            # C_n_k = math.comb(n, k)
            c_mf_1 = m_f
            c_mf_2 = math.comb(m_f, 2)
            c_mm_1 = m_m
            c_pm_1 = p_m
            c_pm_2 = math.comb(p_m, 2)

            # Tính kết quả từng trường hợp
            # Trường hợp 1: Chọn 1 nữ (Toán), 2 nam (phải có Vật lý)
            # Các khả năng cho 2 nam: (1 Toán, 1 Lý) hoặc (2 Lý)
            case1 = c_mf_1 * (c_mm_1 * c_pm_1 + c_pm_2)

            # Trường hợp 2: Chọn 2 nữ (Toán), 1 nam (phải là Vật lý để đủ 2 môn)
            case2 = c_mf_2 * c_pm_1

            kq_dung = case1 + case2

            # Tạo các phương án sai
            s = set()
            while len(s) < 3:
                sai = kq_dung + random.choice([-20, -10, 10, 20, 30, 40, 50])
                if sai > 0 and sai != kq_dung:
                    s.add(sai)

            list_sai = list(s)
            das1 = list_sai[0]
            das2 = list_sai[1]
            das3 = list_sai[2]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một trường cấp 3 có $%s$ giáo viên Toán gồm có $%s$ nữ và $%s$ nam, giáo viên Vật lý thì có $%s$ giáo viên nam. Hỏi có bao nhiêu cách chọn ra một đoàn thanh tra công tác ôn thi tốt nghiệp THPT gồm 3 người có đủ 2 môn Toán và Vật lý và phải có giáo viên nam và giáo viên nữ trong đoàn?'''
                             %(latex(m_total), latex(m_f), latex(m_m), latex(p_m)))

            # Các đáp án
            da_d = ('\\True ' + str(kq_dung))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Vì chọn ra 3 người mà yêu cầu phải có giáo viên nam và giáo viên nữ trong đoàn nên số giáo viên nữ được chọn chỉ có thể bằng 1 hoặc 2. Ta xét hai trường hợp:\\\\
            * Trường hợp 1: Chọn 1 giáo viên nữ: Có $C_{%s}^1$ cách. Khi đó:\\\\
            - Chọn 1 giáo viên nam môn Toán và 1 nam môn Vật lý: Có $C_{%s}^1 \\times C_{%s}^1$ cách.\\\\
            - Chọn 2 giáo viên nam môn Vật lý: Có $C_{%s}^2$ cách.\\\\
            Trường hợp này có $C_{%s}^1 \\left( C_{%s}^1 \\times C_{%s}^1 + C_{%s}^2 \\right) = %s$ cách chọn.\\\\
            * Trường hợp 2: Chọn 2 giáo viên nữ: Có $C_{%s}^2$ cách chọn. Khi đó chọn thêm 1 giáo viên nam môn Vật lý: Có $C_{%s}^1$ cách. Trường hợp này có $C_{%s}^2 \\times C_{%s}^1 = %s$ cách chọn.\\\\
            Vậy tất cả có $%s + %s = %s$ cách chọn.'''
                       %(latex(m_f), 
                         latex(m_m), latex(p_m), 
                         latex(p_m), 
                         latex(m_f), latex(m_m), latex(p_m), latex(p_m), latex(case1),
                         latex(m_f), 
                         latex(p_m), 
                         latex(m_f), latex(p_m), latex(case2),
                         latex(case1), latex(case2), latex(kq_dung)
                        ))

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

