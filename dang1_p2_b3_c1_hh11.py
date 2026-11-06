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


def bt_dang1_p2_b3_c1_hh11(self):
            # Khai báo biến
            hinhve = ('\\begin{center} \n'
            '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-0.6084680038416383,-0.7856324825288481) rectangle (8.127975575807513,5.923570045489017);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,2.)-- (7.,2.);\n'
            '\\draw (2.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (7.,2.);\n'
            '\\draw (2.,0.)-- (1.,2.);\n'
            '\\draw (3.,5.)-- (1.,2.);\n'
            '\\draw (2.,0.)-- (3.,5.);\n'
            '\\draw (3.,5.)-- (4.,0.);\n'
            '\\draw (3.,5.)-- (7.,2.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.)-- (5.5,1.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (3.,5.)-- (4.,2.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (4.,2.)-- (5.5,1.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (4.,2.)-- (1.5,1.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.6666666666666667,3.)-- (5.666666666666667,3.);\n'
            '\\draw (2.738088652819547,5.6) node[anchor=north west] {$S$};\n'
            '\\draw (0.4534201660604686,2.4) node[anchor=north west] {$A$};\n'
            '\\draw (1.45,0.17972039920034105) node[anchor=north west] {$B$};\n'
            '\\draw (3.799976822721654,0.0349174669409627) node[anchor=north west] {$C$};\n'
            '\\draw (7.082176620600894,2.432210456568449) node[anchor=north west] {$D$};\n'
            '\\draw (0.8,1.2576977837979355) node[anchor=north west] {$M$};\n'
            '\\draw (5.50543358044322,1.2094301397114762) node[anchor=north west] {$N$};\n'
            '\\draw (4.009136613762978,2.6) node[anchor=north west] {$P$};\n'
            '\\draw (3.59081703168033,3.6) node[anchor=north west] {$G$};\n'
            '\\draw (1.1935240420528461,3.654990773425422) node[anchor=north west] {$E$};\n'
            '\\draw (5.682414942093571,3.6) node[anchor=north west] {$F$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,2.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,0.)-- (7.,2.);\n'
            '\\draw (5.666666666666667,3.)-- (5.5,1.);\n'
            '\\draw (1.6666666666666667,3.)-- (1.5,1.);\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n')
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang, $AD//BC$, $AD=3BC$. $M,N,P$ lần lượt là trung điểm $AB,CD,AD$. $G$ là trọng tâm $\\Delta SAD$. \n'''

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $MN//(SAD)$'
            nb_da_1_s = '$MN//(SAB)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $MN//(SBC)$'
            nb_da_2_s = '$MN//(SCD)$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có $MN//AD \\subset (SAD) \\Rightarrow MN//(SAD)$.'
                        )
            loigiai_nb_2 = ('Ta có $MN//BC \\subset (SBC) \\Rightarrow MN//(SBC)$.'
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
            th_da_1_d = '\\True $PN//(SAC)$'
            th_da_1_s = '$PN//(SAB)$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $PM//(SBD)$'
            th_da_2_s = '$PM//(SCD)$'
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Xét tam giác $DAC$ có $PN$ là đường trung bình nên $PN//AC$ mà $AC\\subset (SAC)$. \\\\ \n'
                            'Vậy $PN//(SAC)$.'
                        )
            loigiai_th_2 = ('Xét tam giác $ABD$ có $PM$ là đường trung bình nên $PM//BD$ mà $BD\\subset (SBD)$. \\\\ \n'
                            'Vậy $PM//(SBD)$.'
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
            vd_da_1_d = '\\True $(GMN)\\cap (SAB)=EM$ với $E\\in SA;SE=2AE$'
            vd_da_1_s = '$(GMN)\\cap (SAB)=EM$ với $E\\in SA;SE=AE$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $(GMN)\\cap (SCD)=FN$ với $F\\in SD;SF=2FD$'
            vd_da_2_s = '$(GMN)\\cap (SCD)=FN$ với $F\\in SD;SF=FD$'
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có $(GMN)//AD$ nên giao tuyến của $(GMN)$ và $SAD$ là đường thẳng $EF$ qua $G$ và song song với $AD$, thiết diện là tứ giác $MNFE$ và vì cùng song song với $AD$ nên $MN//EF//AD$. \\\\ \n'
                            'Khi đó $\\dfrac{SE}{SA}=\\dfrac{SG}{SP}=\\dfrac{2}{3} \\Rightarrow E\\in SA;SE=2AE$.'
                        )
            loigiai_vd_2 = ('Ta có $(GMN)//AD$ nên giao tuyến của $(GMN)$ và $SAD$ là đường thẳng $EF$ qua $G$ và song song với $AD$, thiết diện là tứ giác $MNFE$ và vì cùng song song với $AD$ nên $MN//EF//AD$. \\\\ \n'
                            'Khi đó $\\dfrac{SF}{SD}=\\dfrac{SG}{SP}=\\dfrac{2}{3} \\Rightarrow F\\in SD;SF=2FD$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Mặt phẳng $(GMN)$ cắt hình chóp $S.ABCD$ theo thiết diện là hình bình hành'
            vdc_da_1_s = 'Mặt phẳng $(GMN)$ cắt hình chóp $S.ABCD$ theo thiết diện là hình chữ nhật'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Mặt phẳng $(GMN)$ cắt hình chóp $S.ABCD$ theo thiết diện là hình bình hành'
            vdc_da_2_s = 'Mặt phẳng $(GMN)$ cắt hình chóp $S.ABCD$ theo các đoạn giao tuyến tạo thành một hình thoi'
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta có $(GMN)//AD$ nên giao tuyến của $(GMN)$ và $SAD$ là đường thẳng $EF$ qua $G$ và song song với $AD$, thiết diện là tứ giác $MNFE$ và vì cùng song song với $AD$ nên $MN//EF\\text{  }(1)$. \\\\ \n'
                            'Đặt $BC=a$ khi đó $AD=3a$ nên $MN=2a$.\\\\ \n'
                            'Vì $G$ là trọng tâm tam giác $SAD$ nên $\\dfrac{EF}{AD}=\\dfrac{2}{3}\\Rightarrow EF=2a$. Vậy $MN=EF$ $(2)$.\\\\ \n'
                            'Từ $(1)$ và $(2)$ suy ra, $MNEF$ là hình bình hành.'
                        )
            loigiai_vdc_2 = ('Ta có $(GMN)//AD$ nên giao tuyến của $(GMN)$ và $SAD$ là đường thẳng $EF$ qua $G$ và song song với $AD$, thiết diện là tứ giác $MNFE$ và vì cùng song song với $AD$ nên $MN//EF\\text{  }(1)$. \\\\ \n'
                            'Đặt $BC=a$ khi đó $AD=3a$ nên $MN=2a$.\\\\ \n'
                            'Vì $G$ là trọng tâm tam giác $SAD$ nên $\\dfrac{EF}{AD}=\\dfrac{2}{3}\\Rightarrow EF=2a$. Vậy $MN=EF$ $(2)$.\\\\ \n'
                            'Từ $(1)$ và $(2)$ suy ra, $MNEF$ là hình bình hành.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\loigiai{ '+str(hinhve)+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

