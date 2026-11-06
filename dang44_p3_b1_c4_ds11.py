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


def bt_dang44_p3_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random thời gian ban đầu t1 (giây)
                t1 = randint(3, 8) 

                # Random mẫu số của công bội q (thường là 10, 12, 15... để kết quả đẹp)
                mau_q = random.choice([10, 12, 15, 20, 30])
                tu_q = mau_q - 1
                q = Rational(tu_q, mau_q)

                # Tính tổng thời gian T (giây) theo công thức cấp số nhân lùi vô hạn: T = t1 / (1 - q)
                # Vì 1 - q = 1/mau_q nên T = t1 * mau_q
                kq_giay = t1 * mau_q

                # Đổi ra phút
                kq_phut = Rational(kq_giay, 60)

                # Định dạng kết quả hiển thị
                if kq_phut.denominator == 1:
                    kq_hien_thi = str(kq_phut)
                    val_kq = int(kq_phut)
                else:
                    # Nếu là phân số, lấy xấp xỉ 1 chữ số thập phân
                    val_kq = float(kq_phut)
                    kq_hien_thi = str(round(val_kq, 1)).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % kq_hien_thi

                # Tạo các đáp án nhiễu
                s = [
                    '$%s$' % (str(val_kq + 1).replace('.', ',')),
                    '$%s$' % (str(val_kq + 2).replace('.', ',')),
                    '$%s$' % (str(val_kq + 0.5).replace('.', ',')),
                    '$%s$' % (str(val_kq - 1) if val_kq > 1 else "0,5").replace('.', ','),
                    '$%s$' % (str(val_kq - 0.5) if val_kq > 0.5 else "0,2").replace('.', ','),
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Nam đang ngồi học thì nghe có tiếng mưa rơi. Tiếng mưa rơi lộp độp nhặt dần đến khi Nam nghe gần như đều đặn. Thời gian đầu tiên Nam ước chừng khoảng $%s$ giây. Sau đó thời gian liên tiếp giảm theo tỉ số là $\\frac{%s}{%s}$. Thời gian Nam bắt đầu nghe các tiếng mưa rơi gần như đều đặn là bao nhiêu phút?'''
                                 % (latex(t1), latex(tu_q), latex(mau_q)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $t_1$ là thời gian giữa 2 tiếng mưa rơi đầu tiên và kế tiếp. \\\\
                            $t_2$ là thời gian giữa 2 tiếng mưa rơi thứ hai và kế tiếp. \\\\
                            ... \\\\
                            $t_n$ là thời gian giữa 2 tiếng mưa rơi thứ $n$ và kế tiếp. \\\\
                            Theo đề ra ta có dãy số $(t_n)$ tạo thành cấp số nhân lùi vô hạn với số hạng đầu tiên là $t_1 = %s s$, công bội $q = \\frac{%s}{%s}$. \\\\
                            Vậy thời gian Nam bắt đầu nghe các tiếng mưa rơi gần như đều đặn là tổng của cấp số nhân lùi vô hạn: \\\\
                            $T = \\frac{t_1}{1 - q} = \\frac{%s}{1 - \\frac{%s}{%s}} = %s \\text{ (giây)} = %s \\text{ (phút)}.$'''
                           % (latex(t1), latex(tu_q), latex(mau_q), 
                              latex(t1), latex(tu_q), latex(mau_q), 
                              latex(kq_giay), latex(kq_phut if kq_phut.denominator != 1 else int(kq_phut))))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_phut if kq_phut.denominator != 1 else int(kq_phut)))

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

