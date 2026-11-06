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


def bt_dang12_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên cho bài toán
            k = random.randint(1, 2)
            h_m_options = {1: [200, 300], 2: [200, 400]}
            h_m = random.choice(h_m_options[k])
            h = h_m / 1000.0

            d_AB = 5 * k
            R_A = 3 * k
            R_B = 4 * k
            d_AC = 3 * k
            d_BC = 4 * k
            d_a = 1 * k
            R_A_new = 2 * k
            h_F2_m = 100 * k
            h_F2 = h_F2_m / 1000.0
            d_F2 = 3 * k

            # Chuẩn bị số liệu string thập phân có dấu phẩy
            h_str = str(h).replace('.', ',')
            x_B = 5 * k
            R_B_sq = (4 * k)**2
            u_x = int(1.8 * k / h)
            u_y = int(2.4 * k / h)
            x_M = 1.2 * k
            y_M = 1.6 * k

            # Nội dung câu hỏi
            noidungcauhoi = ('''Hai trạm phát sóng $A$ và $B$ được đặt cách nhau $%s$km trên một vùng đất bằng phẳng. Để đảm bảo phủ sóng tốt, cả hai trạm đều được xây trên các trụ cao $%s$m. Trạm $A$ có bán kính phát sóng $%s$km, và trạm $B$ có bán kính phát sóng $%s$km. Trên mặt đất có nút giao hai con đường ở vị trí $C$ cách chân hai trạm phát sóng $A$ và $B$ lần lượt là $%s$km và $%s$km. Hai flycam $F_1$ và $F_2$ luôn hoạt động trong vùng phủ sóng của trạm $A$ và trạm $B$ tương ứng. Một ô tô đang di chuyển trên con đường thẳng nối từ chân trạm $A$ đến $C$, rồi cua vào đường thẳng từ $C$ đến chân trạm $B$. Gắn hệ trục tọa độ $Oxyz$ với điểm $O$ trùng với chân trạm $A$, mặt phẳng $(Oxy)$ là mặt đất, tia $Oz$ hướng thẳng đứng lên, chân trạm $B$ nằm trên tia $Ox$ và điểm $C$ có tung độ dương. Đơn vị mỗi trục tọa độ là $1$km.'''               
                             % (d_AB, h_m, R_A, R_B, d_AC, d_BC))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Phương trình biểu thị vùng phát sóng của trạm $B$ là phương trình mặt cầu $(S)$: $(x-%s)^2 + y^2 + (z-%s)^2 = %s$' % (x_B, h_str, R_B_sq)
            nb_da_1_s = 'Phương trình biểu thị vùng phát sóng của trạm $B$ là phương trình mặt cầu $(S)$: $(x+%s)^2 + y^2 + (z-%s)^2 = %s$' % (x_B, h_str, R_B_sq)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Trạm $B$ nằm trên tia $Ox$ cách $O$ (chân trạm $A$) là $%s$km, trụ cao $%sm = %s$km nên tọa độ trạm $B$ là $(%s; 0; %s)$. \\\\
            Vùng phát sóng của trạm $B$ là mặt cầu tâm $B$ bán kính $R_B = %s$km. \\\\
            Vậy phương trình mặt cầu là $(x-%s)^2 + y^2 + (z-%s)^2 = %s$.'''
                        % (d_AB, h_m, h_str, x_B, h_str, R_B, x_B, h_str, R_B_sq))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Phương trình đường thẳng $AC$ là: $\\frac{x}{%s} = \\frac{y}{%s} = \\frac{z-%s}{-1}$' % (u_x, u_y, h_str)
            th_da_1_s = 'Phương trình đường thẳng $AC$ là: $\\frac{x}{%s} = \\frac{y}{%s} = \\frac{z+%s}{-1}$' % (u_x, u_y, h_str)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Chân trạm $A$ là $O(0;0;0)$, trạm $A$ ở độ cao $%s$km nên $A(0;0;%s)$. \\\\
            Gọi $B'$ là chân trạm $B$, ta có $B'(%s;0;0)$. \\\\
            Trong mặt phẳng $(Oxy)$, tam giác $OCB'$ có $OC^2 + B'C^2 = (%s)^2 + (%s)^2 = %s = OB'^2$, nên tam giác vuông tại $C$. \\\\
            Gọi $H$ là hình chiếu của $C$ lên $Ox$, bằng hệ thức lượng ta tính được tọa độ $C(%s; %s; 0)$. \\\\
            Đường thẳng $AC$ đi qua $A(0;0;%s)$ có vectơ chỉ phương $\\overrightarrow{AC} = (%s; %s; -%s) = %s(%s; %s; -1)$. \\\\
            Vậy phương trình đường thẳng $AC$ là $\\frac{x}{%s} = \\frac{y}{%s} = \\frac{z-%s}{-1}$.'''
                       % (h_str, h_str, x_B, d_AC, d_BC, d_AB**2,
                          str(1.8 * k).replace('.', ','), str(2.4 * k).replace('.', ','),
                          h_str,
                          str(1.8 * k).replace('.', ','), str(2.4 * k).replace('.', ','), h_str,
                          h_str, u_x, u_y,
                          u_x, u_y, h_str))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Tính toán cho Vận dụng
            MB_sq = (x_B - x_M)**2 + (0 - y_M)**2 + h**2
            MB_val = math.sqrt(MB_sq)
            MB_sq_str = str(round(MB_sq, 2)).replace('.', ',')

            # Các đáp án
            vd_da_1_d = '\\True Khi ô tô đang ở vị trí cách nút giao $C$ $%s$km trên đoạn đường từ chân trạm $A$ tới nút giao $C$ đến. Khi đó ô tô không nằm trong vùng phát sóng của trạm $B$' % (d_a)
            vd_da_1_s = 'Khi ô tô đang ở vị trí cách nút giao $C$ $%s$km trên đoạn đường từ chân trạm $A$ tới nút giao $C$ đến. Khi đó ô tô đang nằm trong vùng phát sóng của trạm $B$' % (d_a)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $M$ là vị trí của ô tô. Nút giao $C$ cách chân trạm $A$ $%s$km, ô tô cách $C$ $%s$km nên cách chân trạm $A$ là $%s$km. \\\\
            Do đó $\\overrightarrow{OM} = \\frac{%s}{%s}\\overrightarrow{OC} \\Rightarrow M(%s; %s; 0)$. \\\\
            Khoảng cách từ ô tô đến trạm $B$ là \\\\$MB = \\sqrt{(%s - %s)^2 + (0 - %s)^2 + (0 - %s)^2} = \\sqrt{%s} \\approx %s$km. \\\\
            Vì $MB > R_B = %s$km nên ô tô không nằm trong vùng phát sóng của trạm $B$.'''
                       % (d_AC, d_a, d_AC - d_a,
                          d_AC - d_a, d_AC, str(x_M).replace('.', ','), str(y_M).replace('.', ','),
                          x_B, str(x_M).replace('.', ','), str(y_M).replace('.', ','), h_str,
                          MB_sq_str, str(round(MB_val, 2)).replace('.', ','), R_B))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Tính toán cho VDC
            KO = d_AC
            KB_prime = d_BC
            r2_sq = d_F2**2 - (h - h_F2)**2
            r2 = math.sqrt(r2_sq)
            dist_C_A = math.sqrt(KO**2 + h**2)
            dist_C_I2 = math.sqrt(KB_prime**2 + h_F2**2)
            max_dist = dist_C_A + dist_C_I2 + R_A_new + r2
            max_dist_str = str(round(max_dist, 2)).replace('.', ',')
            fake_max_dist_str = str(round(max_dist - 1, 2)).replace('.', ',')

            # Các đáp án
            vdc_da_1_d = '\\True Do thời tiết xấu, trạm $A$ giảm công suất phát làm giảm bán kính phủ sóng xuống còn $%s$km. Biết rằng flycam $F_2$ luôn bay ở độ cao $%sm$ so với mặt đất và cách trạm $B$ một khoảng không đổi là $%s$km. Tổng khoảng cách lớn nhất giữa ô tô và 2 flycam có thể đạt được là $%s$km (làm tròn đến hàng phần trăm)' % (R_A_new, h_F2_m, d_F2, max_dist_str)
            vdc_da_1_s = 'Do thời tiết xấu, trạm $A$ giảm công suất phát làm giảm bán kính phủ sóng xuống còn $%s$km. Biết rằng flycam $F_2$ luôn bay ở độ cao $%sm$ so với mặt đất và cách trạm $B$ một khoảng không đổi là $%s$km. Tổng khoảng cách lớn nhất giữa ô tô và 2 flycam có thể đạt được là $%s$km (làm tròn đến hàng phần trăm)' % (R_A_new, h_F2_m, d_F2, fake_max_dist_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tập hợp các vị trí của $F_1$ là mặt cầu tâm $A(0;0;%s)$ bán kính $R_1 = %s$. \\\\
            Tập hợp các vị trí của $F_2$ là đường tròn $(C_2)$ nằm trên mặt phẳng $z = %s$, có tâm $I_2(%s; 0; %s)$ và bán kính $r_2 = \\sqrt{%s^2 - (%s - %s)^2} = \\sqrt{%s}$. \\\\
            Gọi $K$ là vị trí của ô tô, $K$ thuộc gấp khúc $O \\rightarrow C \\rightarrow B'$. \\\\
            Tổng khoảng cách từ ô tô đến 2 flycam là $d = KF_1 + KF_2 \\le (KA + R_1) + (KI_2 + r_2)$. \\\\
            Ta có $KA = \\sqrt{KO^2 + %s^2}$ và $KI_2 = \\sqrt{KB'^2 + %s^2}$. \\\\
            Bằng cách kiểm tra các điểm tại $O, C, B'$ ta thấy $KA + KI_2$ đạt giá trị lớn nhất khi $K \\equiv C$. \\\\
            Khi đó $KA = \\sqrt{%s^2 + %s^2}$, $KI_2 = \\sqrt{%s^2 + %s^2}$. \\\\
            Khoảng cách lớn nhất là $d_{max} = \\sqrt{%s^2 + %s^2} + \\sqrt{%s^2 + %s^2} + %s + \\sqrt{%s} \\approx %s$km.'''
                       % (h_str, R_A_new,
                          str(h_F2).replace('.', ','), x_B, str(h_F2).replace('.', ','),
                          d_F2, h_str, str(h_F2).replace('.', ','), str(round(r2_sq, 4)).replace('.', ','),
                          h_str, str(h_F2).replace('.', ','),
                          KO, h_str, KB_prime, str(h_F2).replace('.', ','),
                          KO, h_str, KB_prime, str(h_F2).replace('.', ','), R_A_new, str(round(r2_sq, 4)).replace('.', ','), max_dist_str))

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

