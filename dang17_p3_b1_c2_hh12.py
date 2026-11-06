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


def bt_dang17_p3_b1_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập bộ vector pháp tuyến (1, 2, 2) để căn bậc hai của A^2 + B^2 + C^2 = 3 (số nguyên đẹp)
                A, B, C = 1, 2, 2
                mau_so = 3

                # Để chiều cao d nằm trong khoảng [3, 3.5], tử số |D1 - D2| phải nằm trong khoảng [9, 10.5]
                # Chọn delta_d là số nguyên 9 hoặc 10 để phương trình mặt phẳng nhìn "sạch" hơn
                delta_d = random.choice([9, 10])

                d1 = random.randint(-10, 10)
                d2 = d1 - delta_d

                # Tính toán chiều cao h
                h_val = Rational(delta_d, mau_so)
                h_float = float(h_val)

                # Định dạng hiển thị số thập phân kiểu Việt Nam (dấu phẩy)
                def v_format(val):
                    res = str(round(float(val), 2)).replace('.', ',')
                    if res.endswith(',0'): res = res[:-2]
                    return res

                kq_dung = v_format(h_val)

                # Tạo các đáp án sai (đảm bảo không trùng đáp án đúng)
                s_list = []
                while len(s_list) < 3:
                    # Tạo sai số ngẫu nhiên
                    sai_so = random.choice([-1, 1, -0.5, 0.5, 2])
                    v_sai = v_format(h_float + sai_so)
                    if v_sai != kq_dung and v_sai not in s_list:
                        s_list.append(v_sai)

                # Các đáp án trắc nghiệm
                da_d = '\\True $' + kq_dung + '$'
                da_s1 = '$' + s_list[0] + '$'
                da_s2 = '$' + s_list[1] + '$'
                da_s3 = '$' + s_list[2] + '$'

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho hai mặt phẳng song song lần lượt chứa sàn và trần của một căn phòng là $(\\alpha): x + 2y + 2z %s = 0$ và $(\\beta): x + 2y + 2z %s = 0$. Chiều cao (đơn vị: m) của căn phòng bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 %((' + ' + str(d1) if d1 > 0 else ' - ' + str(abs(d1))) if d1 != 0 else "",
                                   (' + ' + str(d2) if d2 > 0 else ' - ' + str(abs(d2))) if d2 != 0 else ""))

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Điểm M thuộc mặt phẳng (beta). Chọn y=0, z=0 => x = -d2
                m_x, m_y, m_z = -d2, 0, 0

                # Lời giải chi tiết
                loigiai = ('''Phương trình mặt phẳng chứa mặt sàn là $(\\alpha): x + 2y + 2z %s = 0$. \\\\
                            Phương trình mặt phẳng chứa trần nhà là $(\\beta): x + 2y + 2z %s = 0$. \\\\
                            Chiều cao của căn phòng chính là khoảng cách giữa hai mặt phẳng song song $(\\alpha)$ và $(\\beta)$. \\\\
                            Lấy điểm $M(%s; 0; 0)$ thuộc mặt phẳng $(\\beta)$. \\\\
                            Chiều cao của căn phòng là: \\\\
                            $h = d(M, (\\alpha)) = \\frac{|%s + 2 \\cdot 0 + 2 \\cdot 0 %s|}{\\sqrt{1^2 + 2^2 + 2^2}} = \\frac{|%s|}{3} = %s$.'''
                            %((' + ' + str(d1) if d1 > 0 else ' - ' + str(abs(d1))) if d1 != 0 else "",
                              (' + ' + str(d2) if d2 > 0 else ' - ' + str(abs(d2))) if d2 != 0 else "",
                              latex(m_x), latex(m_x), 
                              (' + ' + str(d1) if d1 >= 0 else ' - ' + str(abs(d1))),
                              latex(abs(m_x + d1)), kq_dung))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_dung)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

