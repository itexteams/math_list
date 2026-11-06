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


def bt_dang15_p2_b1_c2_ds10(self):
            # Khai báo biến
            def format_money(amount):
                return "{:,.0f}".format(amount).replace(",", ".")

            # Khai báo biến
            P_k = randint(4, 8) * 100
            e_k = randint(3, 5)
            w_k = randint(4, 6)
            while e_k == w_k:
                w_k = randint(4, 6)

            P = P_k * 1000
            e_price = e_k * 1000
            w_price = w_k * 1000

            P_str = format_money(P)
            e_price_str = format_money(e_price)
            w_price_str = format_money(w_price)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khang là học sinh của trường THPT X, do nhà xa nên Khang đã thuê phòng trọ ở gần trường với giá là $%s$ đồng/tháng. Bên cạnh đó hàng tháng Khang phải trả thêm tiền điện $%s$ đồng/$1\\ kwh$ và tiền nước $%s$ đồng/$1\\ m^3$. Giả sử $x$ và $y$ lần lượt là số $kwh$ điện và số $m^3$ nước Khang sử dụng trong 1 tháng.''' 
                             % (P_str, e_price_str, w_price_str))

            ########################################################################
            # Nhận biết ############################################
            m_months = randint(2, 4)
            total_rent = m_months * P
            total_rent_str = format_money(total_rent)
            false_rent_str = format_money(total_rent + 100000)

            nb_da_1_d = '\\True Số tiền Khang phải trả khi thuê phòng trọ trong $%s$ tháng là $%s$ đồng' % (m_months, total_rent_str)
            nb_da_1_s = 'Số tiền Khang phải trả khi thuê phòng trọ trong $%s$ tháng là $%s$ đồng' % (m_months, false_rent_str)

            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số tiền Khang phải trả khi thuê phòng trọ trong $%s$ tháng (không bao gồm điện nước) là: $%s \\cdot %s = %s$ (đồng).''' 
                        % (m_months, m_months, P_str, total_rent_str))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            limit_k = randint(2, 4) * 100
            limit_total = P + limit_k * 1000
            limit_total_str = format_money(limit_total)
            # Rút gọn cho 1000
            c_val = limit_k

            th_da_1_d = '\\True Bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ để Khang chi trả số tiền trong một tháng không vượt quá $%s$ đồng là $%sx + %sy \\le %s$' % (limit_total_str, e_k, w_k, c_val)
            th_da_1_s = 'Bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ để Khang chi trả số tiền trong một tháng không vượt quá $%s$ đồng là $%sx + %sy \\le %s$' % (limit_total_str, e_k, w_k, c_val - 50)

            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tổng số tiền Khang phải trả trong 1 tháng là: $%s + %s x + %s y$ (đồng). \\\\
            Để tổng số tiền không vượt quá $%s$ đồng, ta có bất phương trình: \\\\
            $%s + %s x + %s y \\le %s \\Leftrightarrow %s x + %s y \\le %s$. \\\\
            Chia cả hai vế cho $1000$, ta được: $%sx + %sy \\le %s$.''' 
                       % (P_str, e_price_str, w_price_str, limit_total_str, P_str, e_price_str, w_price_str, limit_total_str, e_price_str, w_price_str, format_money(limit_k*1000), e_k, w_k, c_val))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            x1 = randint(10, 30)
            y1 = randint(5, 15)
            cost_c = P + e_price * x1 + w_price * y1
            cost_c_str = format_money(cost_c)
            cost_c_false_str = format_money(cost_c + 20000)

            vd_da_1_d = '\\True Tổng số tiền Khang phải trả trong tháng khi sử dụng $%s\\ kwh$ điện và $%s\\ m^3$ nước là $%s$' % (x1, y1, cost_c_str)
            vd_da_1_s = 'Tổng số tiền Khang phải trả trong tháng khi sử dụng $%s\\ kwh$ điện và $%s\\ m^3$ nước là $%s$' % (x1, y1, cost_c_false_str)

            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng số tiền Khang phải trả khi sử dụng $%s\\ kwh$ điện và $%s\\ m^3$ nước là: \\\\
            $%s + %s \\cdot %s + %s \\cdot %s = %s + %s + %s = %s$ (đồng).''' 
                           % (x1, y1, P_str, e_price_str, x1, w_price_str, y1, P_str, format_money(e_price*x1), format_money(w_price*y1), cost_c_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            limit_d = P + randint(3, 5) * 100000
            limit_d_str = format_money(limit_d)

            x2 = randint(30, 50)
            y2 = randint(10, 20)
            cost_d = P + e_price * x2 + w_price * y2

            if cost_d <= limit_d:
                vdc_da_1_d = '\\True Để Khang chi trả số tiền trong một tháng không vượt quá $%s$ đồng, thì Khang nên giới hạn sử dụng lượng điện là $%s\\ kwh$ điện và lượng nước là $%s\\ m^3$' % (limit_d_str, x2, y2)
                vdc_da_1_s = 'Để Khang chi trả số tiền trong một tháng không vượt quá $%s$ đồng, thì Khang không thể sử dụng mức $%s\\ kwh$ điện và $%s\\ m^3$ nước' % (limit_d_str, x2, y2)
                loigiai_vdc_1 = ('''Nếu Khang sử dụng $%s\\ kwh$ điện và $%s\\ m^3$ nước, tổng số tiền phải trả là: \\\\
            $%s + %s \\cdot %s + %s \\cdot %s = %s$ (đồng). \\\\
            Vì $%s \\le %s$ nên mức sử dụng này thỏa mãn yêu cầu chi trả không vượt quá $%s$ đồng.''' 
                           % (x2, y2, P_str, e_price_str, x2, w_price_str, y2, format_money(cost_d), format_money(cost_d), limit_d_str, limit_d_str))
            else:
                vdc_da_1_d = '\\True Để Khang chi trả số tiền trong một tháng không vượt quá $%s$ đồng, thì Khang không thể sử dụng mức $%s\\ kwh$ điện và $%s\\ m^3$ nước' % (limit_d_str, x2, y2)
                vdc_da_1_s = 'Để Khang chi trả số tiền trong một tháng không vượt quá $%s$ đồng, thì Khang nên giới hạn sử dụng lượng điện là $%s\\ kwh$ điện và lượng nước là $%s\\ m^3$' % (limit_d_str, x2, y2)
                loigiai_vdc_1 = ('''Nếu Khang sử dụng $%s\\ kwh$ điện và $%s\\ m^3$ nước, tổng số tiền phải trả là: \\\\
            $%s + %s \\cdot %s + %s \\cdot %s = %s$ (đồng). \\\\
            Vì $%s > %s$ nên mức sử dụng này vượt quá giới hạn $%s$ đồng.''' 
                           % (x2, y2, P_str, e_price_str, x2, w_price_str, y2, format_money(cost_d), format_money(cost_d), limit_d_str, limit_d_str))


            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

