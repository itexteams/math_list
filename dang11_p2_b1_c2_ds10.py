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


def bt_dang11_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Ngẫu nhiên các số liệu bài toán
            num_tn = randint(30, 40)
            num_tl = randint(3, 5)
            target_score = randint(7, 9)

            str_tn = '0,2'
            score_tn = Rational(2, 10)
            score_tl = 1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bạn Khoa làm một bài thi giữa học kỳ I môn Toán. Đề thi gồm %s câu hỏi trắc nghiệm và %s câu hỏi tự luận. Khi làm đúng mỗi câu trắc nghiệm được %s điểm, làm đúng mỗi câu tự luận được 1 điểm. Giả sử bạn Khoa làm đúng $x$ câu trắc nghiệm và $y$ câu tự luận và số điểm bạn Khoa đạt được là ít nhất %s điểm. Khi đó:'''
                            % (num_tn, num_tl, str_tn, target_score))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Bạn Khoa được $%sx$ điểm trắc nghiệm và $y$ điểm tự luận ($0 \\le x \\le %s, 0 \\le y \\le %s, x, y \\in \\mathbb{N}$)' % (str_tn, num_tn, num_tl)
            nb_da_1_s = 'Bạn Khoa được $x$ điểm trắc nghiệm và $%sy$ điểm tự luận ($0 \\le x \\le %s, 0 \\le y \\le %s, x, y \\in \\mathbb{N}$)' % (str_tn, num_tn, num_tl)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số điểm trắc nghiệm bạn Khoa đạt được là $%sx$ (điểm). \\\\
            Số điểm tự luận bạn Khoa đạt được là $y$ (điểm) với $0 \\le x \\le %s, 0 \\le y \\le %s, x, y \\in \\mathbb{N}$.'''
                        % (str_tn, num_tn, num_tl))

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
            th_da_1_d = '\\True Bất phương trình bậc nhất hai ẩn biểu thị số điểm bạn Khoa đạt được là $%sx + y \\ge %s$' % (str_tn, target_score)
            th_da_1_s = 'Bất phương trình bậc nhất hai ẩn biểu thị số điểm bạn Khoa đạt được là $%sx + y \\le %s$' % (str_tn, target_score)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tổng số điểm bạn Khoa đạt được là $%sx + y$ (điểm). \\\\
            Vì số điểm bạn Khoa đạt được là ít nhất %s điểm nên bất phương trình bậc nhất hai ẩn tương ứng là $%sx + y \\ge %s$.'''
                        % (str_tn, target_score, str_tn, target_score))

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
            x1 = randint(5, 15)
            y1 = randint(1, 2)
            val1 = score_tn * x1 + score_tl * y1
            str_val1 = str(float(val1)).replace('.', ',')

            if val1 >= target_score:
                vd_da_1_d = '\\True Cặp $(%s; %s)$ là một nghiệm của bất phương trình bậc nhất hai ẩn $x, y$' % (x1, y1)
                vd_da_1_s = 'Cặp $(%s; %s)$ không phải là nghiệm của bất phương trình bậc nhất hai ẩn $x, y$' % (x1, y1)
            else:
                vd_da_1_d = '\\True Cặp $(%s; %s)$ không phải là nghiệm của bất phương trình bậc nhất hai ẩn $x, y$' % (x1, y1)
                vd_da_1_s = 'Cặp $(%s; %s)$ là một nghiệm của bất phương trình bậc nhất hai ẩn $x, y$' % (x1, y1)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            rel1 = '\\ge' if val1 >= target_score else '<'
            check1 = 'đúng' if val1 >= target_score else 'sai'
            is_sol1 = 'là' if val1 >= target_score else 'không phải là'

            # Nội dung lời giải
            loigiai_vd_1 = ('''Thay $x = %s, y = %s$ vào vế trái của bất phương trình $%sx + y \\ge %s$, ta được: \\\\
            $%s \\cdot %s + %s = %s %s %s$ (mệnh đề %s). \\\\
            Do đó, cặp $(%s; %s)$ %s nghiệm của bất phương trình bậc nhất hai ẩn $x, y$.'''
                        % (x1, y1, str_tn, target_score, str_tn, x1, y1, str_val1, rel1, target_score, check1, x1, y1, is_sol1))

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
            x2 = randint(20, 28)
            y2 = randint(1, 2)
            val2 = score_tn * x2 + score_tl * y2
            str_val2 = str(float(val2)).replace('.', ',')

            if val2 >= target_score:
                vdc_da_1_d = '\\True Bạn Khoa làm đúng %s câu trắc nghiệm và %s câu tự luận thì đạt ít nhất %s điểm' % (x2, y2, target_score)
                vdc_da_1_s = 'Bạn Khoa làm đúng %s câu trắc nghiệm và %s câu tự luận thì đạt ít nhất %s điểm' % (x2, y2, target_score)
            else:
                vdc_da_1_d = '\\True Bạn Khoa làm đúng %s câu trắc nghiệm và %s câu tự luận thì chưa đạt %s điểm' % (x2, y2, target_score)
                vdc_da_1_s = 'Bạn Khoa làm đúng %s câu trắc nghiệm và %s câu tự luận thì đạt ít nhất %s điểm' % (x2, y2, target_score)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            status2 = 'đạt ít nhất' if val2 >= target_score else 'chưa đạt'

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Nếu bạn Khoa làm đúng %s câu trắc nghiệm và %s câu tự luận thì số điểm đạt được là: \\\\
            $%s \\cdot %s + %s = %s$ (điểm). \\\\
            Vì $%s %s %s$ nên bạn Khoa %s %s điểm.'''
                        % (x2, y2, str_tn, x2, y2, str_val2, str_val2, '\\ge' if val2 >= target_score else '<', target_score, status2, target_score))

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
                ' \\choiceTFn \n'
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

