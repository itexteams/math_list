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


def bt_dang18_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thiết lập các thông số cơ bản từ đề bài
            # Để random, ta có thể thay đổi nhẹ các con số nếu muốn, 
            # ở đây giữ nguyên theo ảnh nhưng cấu trúc sẵn sàng để thay đổi.
            suc_chua = random.choice([15000,14000,13000,12000,11000,10000])
            gia_ve_cu = randint(10,15)
            khan_gia_cu = random.choice([9000,9100,9200,9300,9400,9500])
            tang_theo_moi_do = random.choice([1000,900,1100,1200,1300])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một trận bóng đá được tổ chức ở một sân vận động có sức chứa $%s$ người. Với giá vé $%s$ thì trung bình các trận đấu gần đây có $%s$ khán giả. Theo một khảo sát thị trường đã chỉ ra rằng cứ giảm $1$ (USD) mỗi vé thì trung bình số khán giả tăng lên $%s$ người. Gọi $x$ (USD) là giá vé.''' 
                             %(latex(suc_chua), latex(gia_ve_cu), latex(khan_gia_cu), latex(tang_theo_moi_do)))

            ########################################################################
            # a) Số tiền giá vé được giảm
            ########################################################################
            nb_da_1_d = '\\True Số tiền giá vé được giảm là $%s - x$ (USD)' % (latex(gia_ve_cu))
            nb_da_1_s = 'Số tiền giá vé được giảm là $x - %s$ (USD)' % (latex(gia_ve_cu))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Vì giá vé ban đầu là $%s$ và giá vé sau khi giảm là $x$, nên số tiền được giảm là $%s - x$ (USD).''' 
                            % (latex(gia_ve_cu), latex(gia_ve_cu)))

            ########################################################################
            # b) Số khán giả tăng lên
            ########################################################################
            th_da_1_d = '\\True Số khán giả tăng lên là $%s(%s - x)$ (người)' % (latex(tang_theo_moi_do), latex(gia_ve_cu))
            th_da_1_s = 'Số khán giả tăng lên là $%sx$ (người)' % (latex(tang_theo_moi_do))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Cứ giảm $1$ đô thì tăng $%s$ người. Khi giảm $(%s - x)$ đô thì số khán giả tăng thêm là $%s(%s - x)$ người.''' 
                            % (latex(tang_theo_moi_do), latex(gia_ve_cu), latex(tang_theo_moi_do), latex(gia_ve_cu)))

            ########################################################################
            # c) Doanh thu
            ########################################################################
            # Công thức đúng: x * [9500 + 1000(14 - x)] = x * (23500 - 1000x)
            vd_da_1_d = '\\True Doanh thu là $x(23500 - 1000x)$'
            vd_da_1_s = 'Doanh thu là $x(9500 + 1000x)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Tổng số khán giả là: $%s + %s(%s - x) = %s + %s - %sx = 23500 - %sx$. \\\\ Doanh thu bằng giá vé nhân với số khán giả: $R(x) = x(23500 - %sx)$.''' 
                            % (latex(khan_gia_cu), latex(tang_theo_moi_do), latex(gia_ve_cu), latex(khan_gia_cu), latex(tang_theo_moi_do*gia_ve_cu), latex(tang_theo_moi_do), latex(tang_theo_moi_do), latex(tang_theo_moi_do)))

            ########################################################################
            # d) Khoảng giá vé không bị lỗ (Giả sử không bị lỗ là doanh thu >= 0 và số khán giả <= sức chứa)
            ########################################################################
            vdc_da_1_d = '\\True Với giá vé từ $8,5$ đến $14$ (USD) thì sân không bị quá tải sức chứa và doanh thu không âm'
            vdc_da_1_s = 'Giá vé từ $10$ đến $13,5$ thì đơn vị không bị lỗ'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để không vượt quá sức chứa: $23500 - 1000x \\le 15000 \\Leftrightarrow 1000x \\ge 8500 \\Leftrightarrow x \\ge 8,5$. \\\\ Để doanh thu không âm: $x(23500 - 1000x) \\ge 0 \\Leftrightarrow 0 \\le x \\le 23,5$. \\\\ Kết hợp lại, giá vé hợp lý từ $8,5$ đô đến $23,5$ đô (nhưng không quá giá cũ $14$ đô tùy theo ngữ cảnh khảo sát). Do đó khẳng định d) trong ảnh là sai về mặt logic kinh tế học nếu không có chi phí.''' )

            ########################################################################
            # Xử lý Logic Chọn đáp án
            ########################################################################
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

