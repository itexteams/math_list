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


def bt_dang13_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến cấu trúc
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1: Nghiên cứu và random thông số
                # Xác suất thắng của A (p_a) từ 0.51 đến 0.60
                p_a_val = round(random.uniform(0.51, 0.60), 2)
                p_b_val = round(1 - p_a_val, 2)

                # Số ván cần thắng để vô địch
                n_win = 5
                # Số ván A đã thắng (luôn để n_win - 1 để giống logic bài mẫu)
                wa = 4
                # Số ván B đã thắng (ngẫu nhiên từ 1 đến 3)
                wb = random.randint(1, 3)
                # Số ván B cần thắng liên tiếp để lật kèo
                k = n_win - wb

                # Tính toán xác suất
                # Xác suất B thắng là p_b^k
                pb_win_total = p_b_val**k
                # Xác suất A thắng là 1 - pb_win_total
                pa_win_total = 1 - pb_win_total

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_decimal = Decimal(str(pa_win_total)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_hien_thi = str(kq_decimal).replace('.', ',')

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % (kq_hien_thi)

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    sai_val = kq_decimal + Decimal(str(random.choice([-0.05, -0.1, 0.05, 0.1, -0.02, 0.02])))
                    if sai_val > 0 and sai_val < 1 and sai_val != kq_decimal:
                        sai_str = '$%s$' % (str(sai_val).replace('.', ','))
                        if sai_str not in s:
                            s.append(sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (Sử dụng latex cho các biến số)
                noidungcauhoi = ('''Hai bạn $A$ và $B$ tranh chức vô địch trong một cuộc thi cờ tướng. Khi chơi 1 ván cờ, xác suất thắng của $A$ là $%s$ và của $B$ là $%s$. Mỗi ván cờ không có hòa cờ. Người giành chiến thắng là người đầu tiên thắng được $%s$ ván cờ. Tại thời điểm bạn $A$ đã thắng $%s$ ván và bạn $B$ mới thắng $%s$ ván thì xác suất để $A$ giành chiến thắng bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).'''
                                 % (str(p_a_val).replace('.', ','), 
                                    str(p_b_val).replace('.', ','), 
                                    latex(n_win), 
                                    latex(wa), 
                                    latex(wb)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Tính toán các bước trung gian cho lời giải
                pb_mu_k = str(p_b_val).replace('.', ',') + '^{' + str(k) + '}'
                val_pb_win = str(round(pb_win_total, 4)).replace('.', ',')

                loigiai = ('''Do tổng xác suất thắng cờ của $A$ và $B$ trong một ván bằng 1 nên khi $A$ thắng đồng nghĩa với việc $B$ thua, $A$ thua đồng nghĩa với việc $B$ thắng. \\\\
            Ghi nhận tại thời điểm hiện tại: $A$ cần thắng thêm $1$ ván, $B$ cần thắng thêm $%s$ ván nữa để vô địch. \\\\
            Gọi $X$ là biến cố: "$A$ là người chiến thắng" $\\Rightarrow \\overline{X}$ là biến cố: "$B$ là người chiến thắng". \\\\
            $B$ là người chiến thắng khi $B$ thắng liên tiếp $%s$ ván tới, xác suất $P(\\overline{X}) = %s \\approx %s$. \\\\
            Vậy xác suất xảy ra $X$ (để $A$ chiến thắng) là: $P(X) = 1 - P(\\overline{X}) = 1 - %s \\approx %s$.'''
                           % (latex(k), 
                              latex(k), 
                              pb_mu_k, 
                              val_pb_win, 
                              val_pb_win, 
                              kq_hien_thi))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_hien_thi))

            # Xuất câu trắc nghiệm (Không dùng raw string r'' theo yêu cầu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

