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


def bt_dang10_p2_b2_c5_ds10(self):
            # Khai báo biến
            # n3: Số giáo viên nam môn Vật lý
            n1 = randint(2, 4)
            n2 = randint(4, 6)
            n3 = randint(3, 5)
            tong_toan = n1 + n2

            # Tính toán các giá trị cho lời giải
            val_a = n1
            val_b = math.comb(n3, 2)
            val_c_dung = n2 * n3
            val_c_sai = n2 + n3

            # Tính toán cho câu (d)
            # Đoàn 3 người đủ 2 môn và đủ nam nữ. 
            # Vì Vật lý chỉ có nam, nên chắc chắn phải có ít nhất 1 nữ từ môn Toán.
            # TH1: 1 nữ Toán, 1 nam Toán, 1 nam Lý: C(n1,1) * C(n2,1) * C(n3,1)
            # TH2: 2 nữ Toán, 1 nam Lý: C(n1,2) * C(n3,1)
            # TH3: 1 nữ Toán, 2 nam Lý: C(n1,1) * C(n3,2)
            th1 = math.comb(n1, 1) * math.comb(n2, 1) * math.comb(n3, 1)
            th2 = math.comb(n1, 2) * math.comb(n3, 1)
            th3 = math.comb(n1, 1) * math.comb(n3, 2)
            tong_cach = th1 + th2 + th3

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một trường cấp 3 của tỉnh Tuyên Quang có %s giáo viên Toán gồm có %s nữ và %s nam, giáo viên Vật lý thì có %s giáo viên nam. Chọn ra một đoàn thanh tra công tác ôn thi tốt nghiệp THPT gồm 3 người.''' 
                             %(latex(tong_toan), latex(n1), latex(n2), latex(n3)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chọn 1 giáo viên nữ có $C_{%s}^{1}$ cách' %(latex(n1))
            nb_da_1_s = 'Chọn 1 giáo viên nữ có $C_{%s}^{1}$ cách' %(latex(n2))
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Để chọn 1 giáo viên nữ, ta chọn 1 trong %s giáo viên nữ môn Toán. Số cách chọn là $C_{%s}^{1} = %s$.'''
                            %(latex(n1), latex(n1), latex(val_a)))

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Chọn 2 giáo viên nam môn Vật lý có $C_{%s}^{2}$ cách' %(latex(n3))
            th_da_1_s = 'Chọn 2 giáo viên nam môn Vật lý có $A_{%s}^{2}$ cách' %(latex(n3))
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Nội dung lời giải
            loigiai_th_1 = ('''Số cách chọn 2 giáo viên nam trong số %s giáo viên nam môn Vật lý là $C_{%s}^{2} = %s$ cách.''' 
                            %(latex(n3), latex(n3), latex(val_b)))

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Chọn 1 giáo viên nam môn Toán và 1 nam môn Vật lý có $C_{%s}^{1} \\cdot C_{%s}^{1}$ cách' %(latex(n2), latex(n3))
            vd_da_1_s = 'Chọn 1 giáo viên nam môn Toán và 1 nam môn Vật lý có $C_{%s}^{1} + C_{%s}^{1}$ cách' %(latex(n2), latex(n3))
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Để chọn 1 nam Toán và 1 nam Lý, ta thực hiện 2 công đoạn liên tiếp: \\\\
                            - Chọn 1 nam Toán có $C_{%s}^{1}$ cách. \\\\
                            - Chọn 1 nam Lý có $C_{%s}^{1}$ cách. \\\\
                            Theo quy tắc nhân, số cách chọn là $C_{%s}^{1} \\cdot C_{%s}^{1} = %s \\cdot %s = %s$ cách.''' 
                            %(latex(n2), latex(n3), latex(n2), latex(n3), latex(n2), latex(n3), latex(val_c_dung)))

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_val_hien_thi = random.choice([tong_cach, tong_cach - randint(5, 10), tong_cach + randint(5, 10)])
            vdc_da_1_d = '\\True Có %s cách chọn ra một đoàn thanh tra gồm 3 người có đủ 2 môn Toán và Vật lý và phải có giáo viên nam và giáo viên nữ' %(latex(tong_cach))
            vdc_da_1_s = 'Có %s cách chọn ra một đoàn thanh tra gồm 3 người có đủ 2 môn Toán và Vật lý và phải có giáo viên nam và giáo viên nữ' %(latex(vdc_val_hien_thi))

            # Đảm bảo tính Đúng/Sai dựa trên giá trị ngẫu nhiên
            if vdc_val_hien_thi == tong_cach:
                vdc_da_1 = vdc_da_1_d
            else:
                vdc_da_1 = vdc_da_1_s

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Do giáo viên Vật lý chỉ có nam, nên để đoàn có cả nam và nữ thì nhất thiết phải chọn ít nhất một giáo viên nữ từ môn Toán. \\\\
                            Các trường hợp có thể xảy ra: \\\\
                            - Trường hợp 1: 1 nữ Toán, 1 nam Toán, 1 nam Lý. Số cách: $C_{%s}^{1} \\cdot C_{%s}^{1} \\cdot C_{%s}^{1} = %s$. \\\\
                            - Trường hợp 2: 2 nữ Toán, 1 nam Lý. Số cách: $C_{%s}^{2} \\cdot C_{%s}^{1} = %s$. \\\\
                            - Trường hợp 3: 1 nữ Toán, 2 nam Lý. Số cách: $C_{%s}^{1} \\cdot C_{%s}^{2} = %s$. \\\\
                            Tổng số cách chọn là: $%s + %s + %s = %s$ cách.'''
                            %(latex(n1), latex(n2), latex(n3), latex(th1),
                              latex(n1), latex(n3), latex(th2),
                              latex(n1), latex(n3), latex(th3),
                              latex(th1), latex(th2), latex(th3), latex(tong_cach)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng để đảm bảo tính khách quan của đề thi
            while True:
                # Chọn ngẫu nhiên lại từ list đã tạo
                temp_nb = random.choice(list_nb_da_1)
                temp_th = random.choice(list_th_da_1)
                temp_vd = random.choice(list_vd_da_1)
                # Riêng câu VDC đã được gán logic so sánh ở trên

                answers = [temp_nb, temp_th, temp_vd, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    shuffled_answers = answers
                    break

            # Gán lời giải tương ứng
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

