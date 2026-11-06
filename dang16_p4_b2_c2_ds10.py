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


def bt_dang16_p4_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Ngẫu nhiên hóa dữ liệu bài toán
                # Giá vé loại 1 (trẻ em): từ 15000 đến 30000, bước nhảy 5000
                p1 = randint(3, 6) * 5000 
                # Giá vé loại 2 (người lớn): từ 40000 đến 60000, bước nhảy 5000
                p2 = randint(8, 12) * 5000 

                # Doanh thu tối thiểu cần đạt (triệu đồng): từ 12 đến 20 triệu
                dt_trieu = randint(12, 20)
                dt = dt_trieu * 1000000

                # Rút gọn bất phương trình: p1*x + p2*y > dt
                # Chia cả 2 vế cho 1000 để đưa về hệ số nhỏ hơn nhằm xử lý bất phương trình: a*x + b*y > c
                a = p1 // 1000
                b = p2 // 1000
                c = dt // 1000

                # Điểm cắt với các trục để vẽ đồ thị
                y_inter = c / b
                x_inter = c / a

                # Tìm giá trị nguyên nhỏ nhất của x + y trong miền nghiệm (x >= 0, y >= 0, ax + by > c)
                min_continuous = min(y_inter, x_inter)

                # Khảo sát thực tế trong phạm vi các giá trị x, y nguyên để tìm min(x+y) thỏa mãn ax + by > c
                min_sum = m = math.ceil(min_continuous)
                found = False
                while not found:
                    for x_val in range(m + 1):
                        y_val = m - x_val
                        if a * x_val + b * y_val > c:
                            found = True
                            break
                    if not found:
                        m += 1

                kq_dung = m

                # Tạo các phương án sai không trùng với đáp án đúng
                s = [kq_dung + 1, kq_dung + 2, kq_dung - 1, kq_dung - 2, int(x_inter)]
                s = list(set([val for val in s if val > 0 and val != kq_dung]))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Định dạng các phương án hiển thị
                da = '$%s$' % latex(kq_dung)
                da_s1 = '$%s$' % latex(das1)
                da_s2 = '$%s$' % latex(das2)
                da_s3 = '$%s$' % latex(das3)

                # TÍNH TOÁN THÔNG SỐ ĐỂ VẼ HÌNH BẰNG TIKZ
                # Để hình vẽ trực quan trên hệ trục tọa độ nhỏ gọn (scale từ 1-5 đơn vị vẽ), ta scale các giá trị cắt trục
                # Tìm hệ số chia k sao cho giá trị lớn nhất nằm trong khoảng tầm 4 đến 5 cm trên giấy.
                max_val = max(x_inter, y_inter)
                k_scale = max_val / 5.0

                # Tọa độ vẽ của các giao điểm trên trục Ox, Oy sau khi scale
                x_draw = x_inter / k_scale
                y_draw = y_inter / k_scale

                # Định nghĩa các giới hạn của Grid và Trục tọa độ
                xmin, ymin = -1, -1
                xmax, ymax = 6, 6

                # Tạo các lệnh gạch sọc miền nghiệm không thỏa mãn (gạch phần x < 0, y < 0 và phần dưới đường thẳng ax + by = c)
                # Độ dày nét vẽ yêu cầu bắt buộc là 1pt
                hatch_x = '  \\fill[pattern=north west lines, pattern color=gray!60] (%s,%s) rectangle (0,%s);\n' % (latex(xmin), latex(ymin), latex(ymax))
                hatch_y = '  \\fill[pattern=north west lines, pattern color=gray!60] (0,%s) rectangle (%s,0);\n' % (latex(ymin), latex(xmax))
                hatch_line = '  \\fill[pattern=north west lines, pattern color=gray!60] (0,0) -- (%s,0) -- (0,%s) -- cycle;\n' % (latex(x_draw), latex(y_draw))
                draw_line = '  \\draw[line width=1pt, color=red] (-0.5, %s) -- (%s, -0.5);\n' % (latex(y_draw + 0.5/x_draw*y_draw), latex(x_draw + 0.5/y_draw*x_draw))
                label_points = '  \\draw[fill=black] (%s,0) circle (1.5pt) node[below] {$%s$};\n  \\draw[fill=black] (0,%s) circle (1.5pt) node[left] {$%s$};\n' % (latex(x_draw), latex(int(x_inter)), latex(y_draw), latex(int(y_inter)))

                # Tạo chuỗi TikZ hoàn chỉnh ghép vào lời giải
                tikz_code = (
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=0.7, >=stealth]\n'
                            '  \\draw[color=gray!30, thin] (%s,%s) grid (%s,%s);\n'
                            '  \\draw[->, line width=1pt] (%s,0) -- (%s,0) node[right] {$x$};\n'
                            '  \\draw[->, line width=1pt] (0,%s) -- (0,%s) node[above] {$y$};\n'
                            '  \\node at (0,0) [below left] {$O$};\n'
                            '  \\begin{scope}\n'
                            '    \\clip (%s,%s) rectangle (%s,%s);\n'
                            '%s' 
                            '%s' 
                            '%s' 
                            '%s' 
                            '%s'
                            '  \\end{scope}\n'
                            '\\end{tikzpicture}\n'
                            '\\end{center}'
                            % (latex(xmin), latex(ymin), latex(xmax), latex(ymax),
                               latex(xmin), latex(xmax), latex(ymin), latex(ymax),
                               latex(xmin), latex(ymin), latex(xmax), latex(ymax),
                               hatch_x, hatch_y, hatch_line, draw_line, label_points))

                # Câu hỏi
                noidungcauhoi = ('''Nhân dịp tết trung thu, một rạp xiếc tổ chức lưu diễn tại các xã. Vé được bán ra gồm 2 loại: Loại 1 (Dành cho trẻ dưới 13 tuổi): $%s$ đồng/vé; Loại 2 (dành cho người từ 13 tuổi trở lên): $%s$ đồng/vé. Người ta tính toán rằng, để không phải bù lỗ thì số tiền mỗi buổi biểu diễn phải đạt tối thiểu $%s$ triệu đồng. Gọi $x, y$ lần lượt là số vé loại 1 và loại 2 mà rạp xiếc bán được. Trong trường hợp rạp xiếc có lãi, tìm giá trị nhỏ nhất của $x + y$.'''
                                 % (latex(p1), latex(p2), latex(dt_trieu)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải bao gồm cả hình vẽ hình TikZ sinh tự động
                loigiai = ('''Từ giả thiết, rạp xiếc có lãi khi tổng số tiền bán vé lớn hơn số tiền tối thiểu để không bù lỗ. Ta có hệ bất phương trình: \\\\
                             $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %sx + %sy > %s \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %sx + %sy > %s \\end{cases}$. \\\\
                             Biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ: \\\\
                             %s
                             Miền nghiệm của hệ bất phương trình là phần mặt phẳng không bị gạch sọc (không kể các đường biên). \\\\
                             Giá trị nhỏ nhất của biểu thức $x + y$ đạt được tại lân cận các điểm giao điểm của đường thẳng với các trục tọa độ là $\\left(0; \\frac{%s}{%s}\\right)$ và $\\left(\\frac{%s}{%s}; 0\\right)$. \\\\
                             Xét các cặp số nguyên $(x; y)$ nằm trong miền nghiệm, ta tìm được giá trị nguyên nhỏ nhất của $x + y$ thỏa mãn là $%s$.'''
                           % (latex(p1), latex(p2), latex(dt), latex(a), latex(b), latex(c),
                              tikz_code,
                              latex(c), latex(b), latex(c), latex(a), latex(kq_dung)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

