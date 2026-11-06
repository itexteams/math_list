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


def bt_dang2_p2_b2_c2_hh10(self):
            # Khai báo biến
            a=randint(1,9)

            # Nội dung câu hỏi
            noidungcauhoi = 'Cho tam giác $ABC$ đều cạnh bằng $%s$. $M$ là trung điểm cạnh $BC$ và $G$ là trọng tâm của tam giác.'%(latex(a))

            hinhve=('\\begin{center} \n'
                    '\\definecolor{uuuuuu}{rgb}{0.26666666666666666,0.26666666666666666,0.26666666666666666}  \n'
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                        '\\clip(-2.4282356379737817,-1.7543488433381844) rectangle (2.421929472736892,2.6607823738545435); \n'
                        '\\draw [line width=1.pt] (0.,2.)-- (1.7333045428957177,-0.9978253161636396); \n'
                        '\\draw [line width=1.pt] (0.,2.)-- (-1.7112056804404485,-1.0352657239705862); \n'
                        '\\draw [line width=1.pt] (-1.7112056804404485,-1.0352657239705862)-- (1.7333045428957177,-0.9978253161636396); \n'
                        '\\draw [line width=1.pt] (0.,2.)-- (0.,-1.016665622834814); \n'
                        '\\draw (-0.3,2.6) node[anchor=north west] {A}; \n'
                        '\\draw (-2.0117138250310713,-1) node[anchor=north west] {B}; \n'
                        '\\draw (1.5,-1) node[anchor=north west] {C}; \n'
                        '\\draw (0.1079194008329444,0.11537129476020352) node[anchor=north west] {G}; \n'
                        '\\draw (-0.3,-1) node[anchor=north west] {M}; \n'
                        '\\begin{scriptsize}  \n'
                            '\\draw [fill=uuuuuu] (0.,0.) circle (1.0pt); \n'
                        '\\end{scriptsize}  \n'
                    '\\end{tikzpicture}  \n'
                    '\\end{center} \n'
                    )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\vec{AC}+\\vec{CB}=\\vec{AB}$'
            nb_da_1_s = '$\\vec{AC}+\\vec{CB}=\\vec{BA}$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $\\vec{MB}+\\vec{MC}=\\vec{0}$'
            nb_da_2_s = '$\\vec{MB}+\\vec{MC}=\\vec{BC}$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Theo quy tắc ba điểm ta có $\\vec{AC}+\\vec{CB}=\\vec{AB}$.'
                        )
            loigiai_nb_2 = ('Vì $M$ là trung điểm của $BC$ nên $\\vec{MB}+\\vec{MC}=\\vec{0}$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\vec{AB}+\\vec{AC}=2\\vec{AM}$'
            th_da_1_s = '$\\vec{AB}+\\vec{AC}=\\vec{AM}$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\vec{GA}+\\vec{GB}+\\vec{GC}=\\vec{0}$'
            th_da_2_s = '$\\vec{GA}+\\vec{GB}+\\vec{GC}=\\vec{GM}$'
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Theo quy tắc hình bình hành ta có $\\vec{AB}+\\vec{AC}=2\\vec{AM}$.'
                        )
            loigiai_th_2 = ('Vì $G$ là trọng tâm của tam giác nên $\\vec{GA}+\\vec{GB}+\\vec{GC}=\\vec{0}$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $\\left| \\vec{AB}-\\vec{CB} \\right|=%s$' %(latex(a))
            vd_da_1_s = '$\\left| \\vec{AB}-\\vec{CB} \\right|=%s$' %(latex(2*a))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\left| \\vec{AB}-\\vec{CB} \\right|=\\left| \\vec{AB}+\\vec{BC} \\right|=\\left| \\vec{AC} \\right|=AC=%s$.'%(latex(a))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $\\left| \\vec{AB}+\\vec{AC} \\right|=%s$' %(latex(a*sqrt(3)))
            vdc_da_1_s = '$\\left| \\vec{AB}+\\vec{AC} \\right|=%s$' %(latex(a))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\left| \\vec{AB}+\\vec{AC} \\right|=\\left| 2 \\vec{AM} \\right|=2AM=%s$.'%(latex(a*sqrt(3)))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'+hinhve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

